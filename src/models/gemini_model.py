import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    google_api_key = api_key,
    model = "gemini-2.5-flash"
)