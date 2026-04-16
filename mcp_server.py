"""MCP server exposing BM25 search over markdown files in data/.

Run directly for stdio transport:
    python mcp_server.py

Extra deps beyond requirements.txt: `mcp`, `opentelemetry-sdk`.
"""

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

mcp = FastMCP("bm25-search")

_docs = load_documents(DATA_DIR)
_chunks = build_chunks(_docs)
_index = build_index(_chunks)


@mcp.tool()
def search(query: str, top_n: int = 5) -> dict:
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
    mcp.run()
