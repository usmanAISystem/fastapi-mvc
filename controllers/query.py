from google import genai 
from dotenv import load_dotenv 
import os 



load_dotenv()


client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

def get_query_answer(q: str):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite", contents=q
    )
    return {q: response.text}