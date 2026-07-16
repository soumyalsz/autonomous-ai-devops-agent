import os
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

print("--- RUNNING LOCAL DEVOPS AI INTEGRATION ---")

# Read the file contents safely
with open("transaction.js", "r") as f:
    code = f.read()

prompt = f"""You are a Principal DevOps Engineer. Analyze this code:

{code}

Identify the critical semantic bug and provide the corrected code block."""

response = client.chat.completions.create(
    model="qwen2.5:14b",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)