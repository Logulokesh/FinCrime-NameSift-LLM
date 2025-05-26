<h1 align="center">🛡️ Customer Screening Tool</h1>
<p align="center">
  A web-based application to screen individuals against watchlists using vector similarity and LLMs.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Backend-FastAPI-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-Streamlit-ff4b4b?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-informational?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Ollama-orange?style=for-the-badge" />
</p>

---

## 🚀 Features

- 🔍 **Real-time Screening**: Fuzzy match names and optional DOBs against watchlists.
- 📂 **Watchlist Management**: Upload CSV, JSON, or ISO 20022 XML data.
- 🧠 **Risk Analysis**: Vector search with SentenceTransformer & LLM explanations via Ollama.
- 🌑 **Dark-themed UI**: Built with Streamlit for an elegant user experience.
- ⚙️ **Scalable Architecture**: Modular FastAPI services with PostgreSQL + pgvector.

---

## 🧩 Architecture Overview

```mermaid
graph TD
    A[User] -->|Access| B[Streamlit UI]
    B -->|Screen Customer| C[FastAPI: /screening/realtime]
    B -->|Upload Watchlist| D[FastAPI: /watchlist/upload]
    C --> E[ScreeningService]
    D --> E
    E -->|Embedding| F[EmbeddingGenerator]
    E -->|LLM Analysis| G[LLMAnalyzer]
    E -->|Database Ops| H[PostgreSQL + pgvector]
    H -->|Results| E --> C --> B
