import os
import torch
import PyPDF2
from sentence_transformers import SentenceTransformer
import chromadb
from litellm import completion
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.tools import ArxivQueryRun
from dotenv import load_dotenv

device = torch.device("cpu") 
client = chromadb.PersistentClient(path="chroma_db")
text_embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
arxiv_tool = ArxivQueryRun()

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")



def extract_text_from_pdfs(uploaded_files):
    all_text = ""
    for uploaded_file in uploaded_files:
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            all_text += page.extract_text() or ""
    return all_text

def process_text_and_store(all_text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50, separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_text(all_text)

    try:
        client.delete_collection(name="knowledge_base")
    except Exception:
        pass

    collection = client.create_collection(name="knowledge_base")

    for i, chunk in enumerate(chunks):
        embedding = text_embedding_model.encode(chunk)
        collection.add(
            ids=[f"chunk_{i}"],
            embeddings=[embedding.tolist()],
            metadatas=[{"source": "pdf", "chunk_id": i}],
            documents=[chunk]
        )
    return collection


# ------------------- Semantic Search -------------------

def semantic_search(query, collection, top_k=2):
    query_embedding = text_embedding_model.encode(query)
    results = collection.query(
        query_embeddings=[query_embedding.tolist()], n_results=top_k
    )
    return results



def generate_response(query, context):
    prompt = f"Query: {query}\nContext: {context}\nAnswer:"
    response = completion(
        model="gemini-1.5",
        provider="gemini",
        messages=[{"role": "user", "content": prompt}],
        api_key=gemini_api_key
    )
    return response['choices'][0]['message']['content']
