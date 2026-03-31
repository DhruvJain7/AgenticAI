# Import the libraries
import json
import os

from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI

# Always include it
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GEMINI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

request = "Please come with a challenging ,nuanced question that I can ask a number of LLMs to evaluate their intelligence."
request += "Answer only with a question , no explanation."
messages = [{"role": "user", "content": request}]

openai = OpenAI()
# Evaluation Question Generated
response = openai.chat.completions.create(
    model="gpt-5-mini",
    messages=messages,
)
question = response.choices[0].message.content
