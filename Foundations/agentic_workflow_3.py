import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI()
question = "Pick a business idea area that might be worth exploring for Agentic AI opportunity?"
messages = [{"role": "user", "content": question}]
response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)
# print(response.choices[0].message.content)
business_idea = response.choices[0].message.content
messages = [{"role": "user", "content": business_idea}]
response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)
print(response.choices[0].message.content)
