import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("api_key is missing")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages: list[ChatCompletionMessageParam] = [
    {
        "role": "user",
        "content": args.user_prompt,
    }
]

response = client.chat.completions.create(
    model="google/gemini-2.5-flash",
    messages=messages,
)

if not response.usage:
    raise RuntimeError(f"API error: {response}")

print(f"""
    Prompt tokens: {response.usage.prompt_tokens}
    Response tokens: {response.usage.completion_tokens}
    """)

print(response.choices[0].message.content)
