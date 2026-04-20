import os
from langchain_groq import ChatGroq

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)