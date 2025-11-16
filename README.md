# 🧠 RAG-Powered Research Paper Assistant

An intelligent **Retrieval-Augmented Generation (RAG)** assistant that helps you **analyze and query research papers**.
You can **upload PDFs** or **search arXiv**, and the system will build a semantic knowledge base using **SentenceTransformers** and **ChromaDB**, then answer your questions using **Google Gemini 1.5** through **LiteLLM**.

---

## 🚀 Features

* ✅ Upload and process multiple PDFs
* ✅ Search and summarize academic papers from **arXiv**
* ✅ Semantic text chunking and embedding via **SentenceTransformers**
* ✅ Persistent vector database using **ChromaDB**
* ✅ Context-aware question answering powered by **Gemini 1.5**
* ✅ Easy-to-use web interface built with **Streamlit**

---

## 🗂️ Project Structure

```
📦 rag-research-assistant
 ┣ 📜 main.py                 # Main Streamlit application
 ┣ 📜 tools.py                # Utility functions for PDF processing, embeddings, and search
 ┣ 📜 requirements.txt        # Python dependencies
 ┣ 📜 .env                    # API keys 
 ┗ 📂 chroma_db               # Local persistent ChromaDB folder
```

---

## 🧰 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/IssawiHadjBachar/rag-research-assistant.git
cd rag-research-assistant
```

---

### 2️⃣ Create and Activate a Virtual Environment

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

Ensure you have **Python 3.10+** installed, then run:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```
GEMINI_API_KEY=""
```

**Where to get the key:**

* [Google AI Studio](https://aistudio.google.com/api-keys)

---

## ⚙️ How It Works

1️⃣ **PDF / arXiv Input** → Extracts text from uploaded PDFs or fetches papers from arXiv.

2️⃣ **Text Chunking** → Uses `RecursiveCharacterTextSplitter` to create semantically meaningful chunks.

3️⃣ **Embedding Generation** → Each chunk is converted into a vector using `all-MiniLM-L6-v2` (SentenceTransformers).

4️⃣ **Vector Storage** → Embeddings are saved into a persistent ChromaDB collection (`knowledge_base`).

5️⃣ **Query** → User asks a question. The query is embedded and matched to the most relevant text chunks.

6️⃣ **Response Generation** → The top results are passed as context to Gemini 1.5 to generate a structured and relevant answer.

---

## 🧪 Usage

Run the app with Streamlit:

```bash
streamlit run main.py
```

