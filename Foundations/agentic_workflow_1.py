import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI()
messages = [{"role": "user", "content": "What is 2+2?"}]
response = openai.chat.completions.create(model="gpt-4.1-nano", messages=messages)
print(response.choices[0].message.content)

#
