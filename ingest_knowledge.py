import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Configuration
PDF_FILE = "store_policy.pdf"
DB_PATH = "./chroma_db"

def ingest_data():
    print(f"📄 Loading {PDF_FILE}...")
    
    loader = PyPDFLoader(PDF_FILE)
    documents = loader.load()
    
    # 2. Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    print(f"🧩 Split into {len(chunks)} chunks.")

    # 3. Initialize Embedding Model (Local & Free)
    print("🧠 Initializing Embedding Model (this might take a minute first time)...")
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 4. Save to ChromaDB (Vector Store)
    print("💾 Saving to Vector Database...")
    Chroma.from_documents(
        documents=chunks, 
        embedding=embedding_model, 
        persist_directory=DB_PATH
    )
    
    print(f"✅ Success! Knowledge stored in {DB_PATH}")

if __name__ == "__main__":
    ingest_data()