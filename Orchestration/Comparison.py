import json
import os

from dotenv import load_dotenv
from Evaluation_Question import question
from IPython.display import Markdown, display
from openai import OpenAI

# Always include it
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GEMINI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

openai = OpenAI()
competitors = []
answers = []
messages = [{"role": "user", "content": question}]

# OpenAI LLM
model_1 = "gpt-5-nano"

response = openai.chat.completions.create(model=model_1, messages=messages)
answer = response.choices[0].message.content

competitors.append(model_1)
answers.append(answer)

# GEMINI
gemini = OpenAI(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model_2 = "gemini-2.5-flash"
response1 = openai.chat.completions.create(model=model_1, messages=messages)
answer1 = response1.choices[0].message.content


competitors.append(model_2)
answers.append(answer1)


groq = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")
model3 = "openai/gpt-oss-120b"

response2 = groq.chat.completions.create(model=model3, messages=messages)
answer2 = response2.choices[0].message.content


competitors.append(model3)
answers.append(answer2)
