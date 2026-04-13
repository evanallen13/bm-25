# bm-25

A lightweight BM25 search template for querying a folder of Markdown files.

## Repository layout

```
bm-25/
├── search.py          # BM25 search template (entry point)
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

### Interactive mode

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

### Single-query mode

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