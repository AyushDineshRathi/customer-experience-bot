from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load the DB we just created
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)

# Test Query
query = "What do we offer if a customer is cold?"
print(f"🔍 Querying: '{query}'")

# Search for top 2 matches
results = vector_db.similarity_search(query, k=2)

print("\n--- RETRIEVED CONTEXT ---")
for doc in results:
    print(f"[CHUNK]: {doc.page_content}...")
print("-------------------------")

if len(results) > 0 and "Hot Cocoa" in results[0].page_content:
    print("✅ SUCCESS: Retrieval is working perfectly.")
else:
    print("❌ FAILURE: Could not find relevant context.")