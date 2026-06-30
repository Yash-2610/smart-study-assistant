from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings


load_dotenv()

API = os.getenv("GROQ_API_KEY")

llm = ChatGroq(

    groq_api_key=API,

    model_name="llama-3.3-70b-versatile",

    temperature=0

)

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)