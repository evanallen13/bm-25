# Information Retrieval

Information retrieval (IR) is the process of obtaining relevant information from a large collection
of documents in response to a query.

## BM25 Algorithm

BM25 (Best Match 25) is a probabilistic ranking function widely used in search engines.
It improves upon TF-IDF by incorporating document length normalization and term frequency saturation.

### BM25 Parameters

- **k1** (default ~1.5): Controls term frequency saturation. Higher values give more weight to term frequency.
- **b** (default 0.75): Controls document length normalization. A value of 1.0 fully normalizes by length; 0 disables normalization.

### How BM25 Works

For each query term, BM25 computes a score based on:
1. How often the term appears in the document (term frequency)
2. How rare the term is across all documents (inverse document frequency)
3. The length of the document relative to the average document length

## Other Ranking Algorithms

- **TF-IDF**: Term Frequency–Inverse Document Frequency, a classic baseline
- **BM25+**: A variant of BM25 that addresses the problem of lower-bounding term frequency
- **Neural retrieval**: Dense vector search using sentence embeddings (e.g., FAISS, Annoy)

## Applications

Search engines, question answering systems, document clustering, recommendation systems,
and enterprise knowledge bases all rely on information retrieval techniques.
