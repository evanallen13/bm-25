"""
BM25 search template for markdown files.

Usage:
    python search.py                     # interactive mode
    python search.py "your query here"   # single query mode

Place your .md files in the 'data/' directory next to this script.
Install dependencies first:
    pip install -r requirements.txt
"""

from dataclasses import dataclass
import re
import sys
from pathlib import Path
from rank_bm25 import BM25Okapi

DATA_DIR = Path(__file__).parent / "data"
CHUNK_LINES = 12
CHUNK_OVERLAP = 3


@dataclass(frozen=True)
class Chunk:
    """A searchable text slice tied to a source document and line range."""

    path: Path
    start_line: int
    end_line: int
    text: str


def load_documents(data_dir: Path) -> list[tuple[Path, str]]:
    """Load all markdown files from *data_dir* recursively as (path, text) pairs."""
    paths = sorted(data_dir.rglob("*.md"))
    if not paths:
        raise FileNotFoundError(
            f"No .md files found in '{data_dir}'. "
            "Add markdown files to the data/ directory (including subfolders) and try again."
        )
    return [(p, p.read_text(encoding="utf-8")) for p in paths]


def chunk_text(path: Path, text: str, size: int, overlap: int) -> list[Chunk]:
    """Split text into overlapping line chunks with source line numbers."""
    lines = text.splitlines()
    if not lines:
        return []

    chunks: list[Chunk] = []
    step = max(1, size - overlap)

    for start in range(0, len(lines), step):
        end = min(start + size, len(lines))
        snippet = "\n".join(lines[start:end]).strip()
        if snippet:
            chunks.append(
                Chunk(
                    path=path,
                    start_line=start + 1,
                    end_line=end,
                    text=snippet,
                )
            )
        if end >= len(lines):
            break

    return chunks


def build_chunks(docs: list[tuple[Path, str]]) -> list[Chunk]:
    """Build chunk metadata for all loaded documents."""
    chunks: list[Chunk] = []
    for path, text in docs:
        chunks.extend(chunk_text(path, text, CHUNK_LINES, CHUNK_OVERLAP))
    return chunks


def tokenize(text: str) -> list[str]:
    """Lowercase and split *text* into word tokens, stripping punctuation."""
    return re.findall(r"\b\w+\b", text.lower())


def build_index(chunks: list[Chunk]) -> BM25Okapi:
    """Build a BM25 index from chunk text."""
    tokenized = [tokenize(chunk.text) for chunk in chunks]
    return BM25Okapi(tokenized)


def search(
    index: BM25Okapi,
    chunks: list[Chunk],
    query: str,
    top_n: int = 3,
) -> list[tuple[float, Chunk]]:
    """Return the top-*n* results for *query* as (score, chunk) pairs."""
    tokens = tokenize(query)
    scores = index.get_scores(tokens)
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    return [(score, chunks[idx]) for idx, score in ranked[:top_n] if score > 0]


def print_results(results: list[tuple[float, Chunk]]) -> None:
    """Pretty-print chunk-level search results with source line ranges."""
    if not results:
        print("  No matching documents found.\n")
        return

    for rank, (score, chunk) in enumerate(results, start=1):
        preview = re.sub(r"\s+", " ", chunk.text).strip()
        if len(preview) > 120:
            preview = preview[:117] + "..."
        print(
            f"  {rank}. {chunk.path.name}:{chunk.start_line}-{chunk.end_line} "
            f"(score: {score:.4f})"
        )
        print(f"     {preview}")
    print()


def main() -> None:
    # Load and chunk documents
    print(f"Loading documents from '{DATA_DIR}' ...")
    docs = load_documents(DATA_DIR)
    paths = [path for path, _ in docs]
    chunks = build_chunks(docs)
    print(
        f"Indexed {len(paths)} document(s), {len(chunks)} chunk(s): "
        f"{[p.name for p in paths]}\n"
    )

    # Build BM25 index
    index = build_index(chunks)

    # Single-query mode (argument passed on the command line)
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(f"Query: {query!r}")
        results = search(index, chunks, query)
        print_results(results)
        return

    # Interactive mode
    print("Enter a search query (or 'quit' to exit):")
    while True:
        try:
            query = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not query:
            continue
        if query.lower() in {"quit", "exit", "q"}:
            break
        results = search(index, chunks, query)
        print_results(results)


if __name__ == "__main__":
    main()
