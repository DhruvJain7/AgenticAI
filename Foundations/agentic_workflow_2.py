import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI()
question = "Please pose a challenging question to assess someone's Iq?"

messages = [{"role": "user", "content": question}]
response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)
question = response.choices[0].message.content
messages = [{"role": "user", "content": question}]
# Ask it again

response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)

answer = response.choices[0].message.content
print(answer)
from IPython.display import Markdown, display

display(Markdown(answer))
