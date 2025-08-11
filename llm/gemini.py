from google import genai
from dotenv import load_dotenv
import os

load_dotenv()  # Make sure environment variables are loaded
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def getResponse(content):
    return client.models.generate_content(
        model="gemini-2.0-flash",
        contents=content
    )

