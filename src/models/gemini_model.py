from langchain_google_genai import GoogleGenerativeAI

model = GoogleGenerativeAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    model_name = "gemini-2.0-flash-exp"
)