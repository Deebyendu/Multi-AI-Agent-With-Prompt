import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
    ALLOWED_MODEL_NAME=[
        "llama-3.3-70b-versatile",
        "openai/gpt-oss-120b"
    ]

settings=Settings()

