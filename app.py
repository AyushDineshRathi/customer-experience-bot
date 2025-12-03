import chainlit as cl
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Import our custom modules
from pii_guardrail import mask_pii
from mock_context import get_live_context

# --- CONFIGURATION ---
# We use the model we just downloaded. 
# "temperature=0" makes it factual (less hallucination).
LLM_MODEL = "llama3.2" 

# 1. Load the Memory (RAG)
print("🧠 Loading Knowledge Base...")
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)
retriever = vector_db.as_retriever(search_kwargs={"k": 2})

# 2. Setup the Local Brain (Ollama)
print(f"🤖 Connecting to Local LLM ({LLM_MODEL})...")
llm = ChatOllama(model=LLM_MODEL, temperature=0)

# 3. Define the prompt (The "System Instructions")
template = """
You are a Hyper-Personalized Retail Assistant for a store.

--- REAL-TIME CONTEXT ---
User Profile: {user_context}
Current Environment: {env_context}
Nearby: {location_context}
-------------------------

--- INTERNAL POLICY ---
{rag_context}
-----------------------

USER QUERY (PII Masked): {question}

INSTRUCTIONS:
1. You are talking to the customer directly. Be helpful and brief.
2. Use the "Nearby" context to suggest specific store locations (e.g., "50m away").
3. Use "Environment" to suggest products (e.g., if raining -> umbrella).
4. Answer based ONLY on the context provided above.

YOUR ANSWER:
"""

prompt = ChatPromptTemplate.from_template(template)

@cl.on_chat_start
async def start():
    # This runs when you open the browser
    msg = cl.Message(content="👋 Hello Deepak! I'm your Local Store Assistant (Running Privacy-First). How can I help?")
    await msg.send()

@cl.on_message
async def main(message: cl.Message):
    # STEP 1: PII MASKING (Safety Layer)
    # We protect the user's data BEFORE it even hits the local LLM
    clean_text = mask_pii(message.content)
    
    # Visual Feedback if PII was removed
    if clean_text != message.content:
        await cl.Message(content=f"🛡️ *Privacy Shield Active:* Personal data masked.").send()

    # STEP 2: FETCH LIVE CONTEXT
    live_data = get_live_context()
    
    # STEP 3: RUN THE CHAIN
    # We connect: Retriever -> Context -> Prompt -> Local LLM
    chain = (
        {
            "rag_context": retriever, 
            "question": RunnablePassthrough(),
            "user_context": lambda x: str(live_data['user_profile']),
            "env_context": lambda x: str(live_data['environment']),
            "location_context": lambda x: str(live_data['current_location'])
        }
        | prompt 
        | llm 
        | StrOutputParser()
    )

    # Stream the answer back to the UI
    res = await chain.ainvoke(clean_text)
    await cl.Message(content=res).send()