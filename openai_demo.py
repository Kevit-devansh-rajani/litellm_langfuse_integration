# In this file, I have integrated OpenAI (using LiteLLM) and Langfuse (for tracing)

import litellm
from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGFUSE_PUBLIC_KEY"] = os.getenv("LANGFUSE_PUBLIC_KEY")
os.environ["LANGFUSE_SECRET_KEY"] = os.getenv("LANGFUSE_SECRET_KEY")

litellm.success_callback = ["langfuse"]

user_query = input("Enter your query: ")

messages = [{
    "content": user_query,
    "role": "user"
}]

response = completion(model="openai/gpt-4o", messages=messages)

print(f"Response: {response['choices'][0]['message']['content']}")
