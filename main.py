import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenAI client
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

model = "openai/gpt-4o-mini"
prompt = "What is the capital of England?"

response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)