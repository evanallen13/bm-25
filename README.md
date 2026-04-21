# bm-25

A lightweight BM25 search server for querying a folder of Markdown files, exposed as an [MCP](https://modelcontextprotocol.io) server.

## Repository layout

```
bm-25/
├── mcp_server.py      # MCP server exposing the `search` tool over stdio
├── search.py          # BM25 indexing + search logic (also usable as a CLI)
├── requirements.txt   # Python dependencies
└── data/              # Place your .md files here
    ├── information_retrieval.md
    ├── machine_learning.md
    └── python_intro.md
```

## Setup

1. **Install Python 3.9+** (if not already installed).

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### MCP server

Run the server over stdio:

```bash
python mcp_server.py
```

It registers a single tool, `search(query: str, top_n: int = 3)`, which returns the top-N BM25 matches (score, path, line range, and chunk text) from the markdown corpus in `data/`. OpenTelemetry spans are emitted to stderr so stdout stays clean for JSON-RPC.

Example client config (e.g. `~/.config/claude/mcp.json` or equivalent):

```json
{
  "mcpServers": {
    "bm25-search": {
      "command": "python",
      "args": ["/absolute/path/to/bm-25/mcp_server.py"]
    }
  }
}
```

### Docker

Build the image:

```bash
docker build -t bm25-mcp-server .
```

Configure Claude Desktop to use the containerized server (in `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "bm25-search": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "bm25-mcp-server"]
    }
  }
}
```

### CLI: interactive mode

Run the script without arguments to enter an interactive query loop:

```bash
python search.py
```

```
Loading documents from '.../data' …
Indexed 3 document(s): ['information_retrieval.md', 'machine_learning.md', 'python_intro.md']

Enter a search query (or 'quit' to exit):
> machine learning algorithms
  1. machine_learning.md  (score: 0.4210)
  2. python_intro.md  (score: 0.1898)
  3. information_retrieval.md  (score: 0.0751)

> quit
```

### CLI: single-query mode

Pass a query directly on the command line:

```bash
python search.py "BM25 ranking"
```

```
Loading documents from '.../data' …
Indexed 3 document(s): ['information_retrieval.md', 'machine_learning.md', 'python_intro.md']

Query: 'BM25 ranking'
  1. information_retrieval.md  (score: 1.6854)
```

## Adding your own documents

Drop any `.md` files into the `data/` directory.  
They are automatically discovered and indexed the next time `search.py` is run.

## How it works

1. All `.md` files in `data/` are read and tokenized (lowercased, punctuation stripped).
2. A [BM25Okapi](https://github.com/dorianbrown/rank_bm25) index is built over the token lists.
3. Each query is tokenised the same way, and the top-scoring documents are returned.

BM25 key parameters (can be tuned inside `search.py`):

| Parameter | Default | Effect |
|-----------|---------|--------|
| `k1` | 1.5 | Term-frequency saturation |
| `b` | 0.75 | Document-length normalization |