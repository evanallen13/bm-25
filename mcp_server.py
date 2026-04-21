"""MCP server exposing BM25 search over markdown files in data/.

Run directly for stdio transport:
    python mcp_server.py

Environment variables:
    MCP_TRANSPORT: stdio (default), sse, or streamable-http
    MCP_HOST: bind host for network transports (default 0.0.0.0)
    MCP_PORT: bind port for network transports (default 8000)
    MCP_LOG_LEVEL: FastMCP/uvicorn log level (default INFO)
    MCP_MOUNT_PATH: mount path for SSE app (default /)
    MCP_SSE_PATH: SSE endpoint path (default /sse)
    MCP_MESSAGE_PATH: SSE message endpoint path (default /messages/)
    MCP_STREAMABLE_HTTP_PATH: Streamable HTTP endpoint path (default /mcp)

Extra deps beyond requirements.txt: `mcp`, `opentelemetry-sdk`.
"""

import os
import sys

from mcp.server.fastmcp import FastMCP
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

from search import (
    DATA_DIR,
    build_chunks,
    build_index,
    load_documents,
    search as bm25_search,
)

# Export spans to stderr — stdout is reserved for MCP's JSON-RPC traffic.
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter(out=sys.stderr))
)
tracer = trace.get_tracer(__name__)


def _get_env_int(name: str, default: int) -> int:
    raw_value = os.getenv(name)
    if raw_value is None or not raw_value.strip():
        return default

    try:
        return int(raw_value)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer, got {raw_value!r}") from exc


MCP_TRANSPORT = os.getenv("MCP_TRANSPORT", "stdio").strip().lower()
if MCP_TRANSPORT not in {"stdio", "sse", "streamable-http"}:
    raise ValueError(
        "MCP_TRANSPORT must be one of: stdio, sse, streamable-http "
        f"(got {MCP_TRANSPORT!r})"
    )

MCP_HOST = os.getenv(
    "MCP_HOST", "127.0.0.1" if MCP_TRANSPORT == "stdio" else "0.0.0.0"
)
MCP_PORT = _get_env_int("MCP_PORT", 8000)
MCP_LOG_LEVEL = os.getenv("MCP_LOG_LEVEL", "INFO").upper()
MCP_MOUNT_PATH = os.getenv("MCP_MOUNT_PATH", "/")
MCP_SSE_PATH = os.getenv("MCP_SSE_PATH", "/sse")
MCP_MESSAGE_PATH = os.getenv("MCP_MESSAGE_PATH", "/messages/")
MCP_STREAMABLE_HTTP_PATH = os.getenv("MCP_STREAMABLE_HTTP_PATH", "/mcp")

mcp = FastMCP(
    "bm25-search",
    host=MCP_HOST,
    port=MCP_PORT,
    log_level=MCP_LOG_LEVEL,
    mount_path=MCP_MOUNT_PATH,
    sse_path=MCP_SSE_PATH,
    message_path=MCP_MESSAGE_PATH,
    streamable_http_path=MCP_STREAMABLE_HTTP_PATH,
)

_docs = load_documents(DATA_DIR)
_chunks = build_chunks(_docs)
_index = build_index(_chunks)


@mcp.tool()
def doc_search(query: str, top_n: int = 5) -> dict:
    """Look up documentation to help answer the user's prompt.

    Call this whenever the user's question might be answered by the indexed
    markdown corpus (e.g. GitHub docs, project notes). Pass a focused search
    query derived from the user's prompt — keywords, an API name, an error
    string, or a paraphrased question all work. Use the returned `context`
    as reference material when composing your reply, and cite `sources` so
    the user can verify.

    Returns:
        context: concatenated excerpts, each prefixed with its source path
            and line range — drop this straight into your reasoning.
        sources: structured list of {path, start_line, end_line, score} for
            citation or follow-up reads.
    """
    with tracer.start_as_current_span("bm25.search") as span:
        span.set_attribute("bm25.query", query)
        span.set_attribute("bm25.top_n", top_n)
        results = bm25_search(_index, _chunks, query, top_n=top_n)
        span.set_attribute("bm25.result_count", len(results))

        if not results:
            return {
                "context": f"No documentation matched the query {query!r}.",
                "sources": [],
            }

        sections = [
            f"--- {chunk.path}:{chunk.start_line}-{chunk.end_line} "
            f"(score {score:.3f}) ---\n{chunk.text}"
            for score, chunk in results
        ]
        sources = [
            {
                "path": str(chunk.path),
                "start_line": chunk.start_line,
                "end_line": chunk.end_line,
                "score": score,
            }
            for score, chunk in results
        ]
        return {"context": "\n\n".join(sections), "sources": sources}


if __name__ == "__main__":
    # mount_path is only used for the SSE app variant.
    run_mount_path = MCP_MOUNT_PATH if MCP_TRANSPORT == "sse" else None
    mcp.run(transport=MCP_TRANSPORT, mount_path=run_mount_path)
