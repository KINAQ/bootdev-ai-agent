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
parser.add_argument("--verbose", action="store_true", required=False, help="Enable verbose output")

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

output_lines = []

if args.verbose:
    output_lines.append(f"User prompt: {args.user_prompt}")
    output_lines.append(f"Prompt tokens: {response.usage.prompt_tokens}")
    output_lines.append(f"Response tokens: {response.usage.completion_tokens}")

print("\n".join(output_lines))

print(response.choices[0].message.content)
