"""
BM25 search template for markdown files.

Usage:
    python search.py                     # interactive mode
    python search.py "your query here"   # single query mode

Place your .md files in the 'data/' directory next to this script.
Install dependencies first:
    pip install -r requirements.txt
"""

import re
import sys
from pathlib import Path

from rank_bm25 import BM25Okapi


DATA_DIR = Path(__file__).parent / "data"


def load_documents(data_dir: Path) -> tuple[list[str], list[Path]]:
    """Load all markdown files from *data_dir*.

    Returns a tuple of (texts, paths) where texts[i] is the plain-text
    content of paths[i].
    """
    paths = sorted(data_dir.glob("*.md"))
    if not paths:
        raise FileNotFoundError(
            f"No .md files found in '{data_dir}'. "
            "Add markdown files to the data/ directory and try again."
        )
    texts = [p.read_text(encoding="utf-8") for p in paths]
    return texts, paths


def tokenize(text: str) -> list[str]:
    """Lowercase and split *text* into word tokens, stripping punctuation."""
    return re.findall(r"\b\w+\b", text.lower())


def build_index(texts: list[str]) -> BM25Okapi:
    """Build a BM25 index from a list of document texts."""
    tokenized = [tokenize(doc) for doc in texts]
    return BM25Okapi(tokenized)


def search(
    index: BM25Okapi,
    paths: list[Path],
    query: str,
    top_n: int = 5,
) -> list[tuple[float, Path]]:
    """Return the top-*n* results for *query* as (score, path) pairs."""
    tokens = tokenize(query)
    scores = index.get_scores(tokens)
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    return [(score, paths[idx]) for idx, score in ranked[:top_n] if score > 0]


def print_results(results: list[tuple[float, Path]]) -> None:
    """Pretty-print search results."""
    if not results:
        print("  No matching documents found.\n")
        return
    for rank, (score, path) in enumerate(results, start=1):
        print(f"  {rank}. {path.name}  (score: {score:.4f})")
    print()


def main() -> None:
    # Load documents
    print(f"Loading documents from '{DATA_DIR}' …")
    texts, paths = load_documents(DATA_DIR)
    print(f"Indexed {len(paths)} document(s): {[p.name for p in paths]}\n")

    # Build BM25 index
    index = build_index(texts)

    # Single-query mode (argument passed on the command line)
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(f"Query: {query!r}")
        results = search(index, paths, query)
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
        results = search(index, paths, query)
        print_results(results)


if __name__ == "__main__":
    main()
