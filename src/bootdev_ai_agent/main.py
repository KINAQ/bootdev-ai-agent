import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("api_key is missing")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

response = client.chat.completions.create(
    model="google/gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ],
)

if not response.usage:
    raise RuntimeError(f"API error: {response}")

print(f"""
    Prompt tokens: {response.usage.prompt_tokens}
    Response tokens: {response.usage.completion_tokens}
    """)

print(response.choices[0].message.content)
