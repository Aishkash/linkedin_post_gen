from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model="llama-3.1-8b-instant")


if __name__=="__main__":
    response=llm.invoke("What is the capital of France?")
    print(response.content)