from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env vars into environment

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)
