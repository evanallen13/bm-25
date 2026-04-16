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
def search(query: str, top_n: int = 3) -> list[dict]:
    """Return the top-N BM25 matches for *query* from the indexed markdown corpus."""
    with tracer.start_as_current_span("bm25.search") as span:
        span.set_attribute("bm25.query", query)
        span.set_attribute("bm25.top_n", top_n)
        results = bm25_search(_index, _chunks, query, top_n=top_n)
        span.set_attribute("bm25.result_count", len(results))
        return [
            {
                "score": score,
                "path": str(chunk.path),
                "start_line": chunk.start_line,
                "end_line": chunk.end_line,
                "text": chunk.text,
            }
            for score, chunk in results
        ]


if __name__ == "__main__":
    mcp.run()
