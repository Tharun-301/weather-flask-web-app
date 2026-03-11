import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

print(f"API Key found: {'Yes' if api_key else 'No'}")
if api_key:
    print(f"API Key starts with: {api_key[:5]}...")