# 🧠 RAG-Powered Research Paper Assistant

An intelligent **Retrieval-Augmented Generation (RAG)** assistant that helps you **analyze and query research papers**.
You can **upload PDFs** or **search arXiv**, and the system will build a semantic knowledge base using **SentenceTransformers** and **ChromaDB**, then answer your questions using **Google Gemini 1.5** through **LiteLLM**.

---

## 🚀 Features

✅ Upload and process multiple PDFs 
✅ Search and summarize academic papers from **arXiv** 
✅ Semantic text chunking and embedding via **SentenceTransformers** 
✅ Persistent vector database using **ChromaDB** 
✅ Context-aware question answering powered by **Gemini 1.5** 
✅ Easy-to-use web interface built with **Streamlit** 

---

## 🗂️ Project Structure

```
📦 rag-research-assistant
 ┣ 📜 app.py                  # Main Streamlit application
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

Make sure you have **Python 3.10+** installed, then run:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```
GEMINI_API_KEY="" 
HUGGINGFACE_TOKEN=""
```

**Where to get the keys:**

* [Google AI Studio](https://aistudio.google.com/api-keys)
* [Hugging Face](https://huggingface.co/settings/tokens)

---

## 🧪 Usage

Run the app with Streamlit:

```bash
streamlit run main.py
```


---
