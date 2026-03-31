import json
import os

from Comparison import answers, competitors
from dotenv import load_dotenv
from Evaluation_Question import question
from IPython.display import Markdown, display
from openai import OpenAI

# Always include it
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# for competitor, answer in zip(competitors, answers):
#     print(f"Competitor: {competitor}\n\n{answer}")

together = ""
for index, answer in enumerate(answers):
    together += f"#Response from competitor {index + 1}\n\n"
    together += answer + "\n\n"


judge = f"""You are judging a competition between {len(competitors)} competitors.
Each model has been given this question:

{question}

Your job is to evaluate each response for clarity and strength of argument, and rank them in order of best to worst.
Respond with JSON, and only JSON, with the following format:
{{"results": ["best competitor number", "second best competitor number", "third best competitor number", ...]}}

Here are the responses from each competitor:

{together}

Now respond with the JSON with the ranked order of the competitors, nothing else. Do not include markdown formatting or code blocks."""


judge_messages = [{"role": "user", "content": judge}]

openai = OpenAI()
response = openai.chat.completions.create(
    model="gpt-5-mini",
    messages=judge_messages,
)
results = response.choices[0].message.content
results_dict = json.loads(results)
ranks = results_dict["results"]

for index, result in enumerate(ranks):
    competitor = competitors[int(result) - 1]
    print(f"Rank {index + 1}: {competitor}")
