
# 🔍 Haystack Basic QA Pipeline Breakdown – Day 2

## 🔄 Pipeline Flow

### 1. 📄 Document Store

- Used `InMemoryDocumentStore` for testing.
- Stores texts for the retriever to search.

---

### 2. 🔎 Retriever

- Retrieves relevant documents for a given query.
- Uses **BM25** algorithm (can also use dense embedding retrievers like DPR or Elasticsearch).
- Fast but shallow understanding of the context.

---

### 3. 📖 Reader

- Deep model (Transformers-based) that extracts precise answers from documents.
- Model used: `deepset/roberta-base-squad2`
- Takes output from retriever and selects the best answers.

---

### 4. 💬 Pipeline Query

```python
from haystack.pipelines import ExtractiveQAPipeline
pipe = ExtractiveQAPipeline(reader, retriever)

prediction = pipe.run(query="", top_k_retriever=10, top_k_reader=5)
