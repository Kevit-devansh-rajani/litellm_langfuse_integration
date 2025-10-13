from langfuse import Langfuse
import litellm
import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

os.environ["LANGFUSE_PUBLIC_KEY"] = os.getenv("LANGFUSE_PUBLIC_KEY")
os.environ["LANGFUSE_SECRET_KEY"] = os.getenv("LANGFUSE_SECRET_KEY")

litellm.success_callback = ["langfuse"]
litellm.failure_callback = ["langfuse"]

langfuse = Langfuse()

# User Query
user_query = input("Enter your query: ")

# Prompt for System
system_prompt = """
    You are a helpful assistant. You have to give answer user query with greetings.
    Make sure that your answer is correct and very short in length. Only give answer to user whatever asked to you don't give information in depth.
"""

# Messages --> System Prompt & User query
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_query}
]

# Adding traces
trace = langfuse.trace(
    name="user_query_trace",
    input=user_query,
    session_id="cohere-devansh-session1",
    metadata={"userid": "devansh1", "model": "cohere-command-r+"}
)

try:
    response = litellm.completion(
        model="cohere/command-r-plus-08-2024",
        messages=messages
    )

    answer = response['choices'][0]['message']['content']

    trace.update(output=answer)

    trace.score(name="relevance", value=0.9)
    trace.score(name="politeness", value=1.0)
    trace.score(name="conciseness", value=0.8)

    print(f"Response: {answer}")

    # Prompt for LLM-as-a-judge
    eval_prompt = f"""
        You are an evaluator. Rate the following answer for correctness and helpfulness (0-1):
        Question: {user_query}
        Answer: {answer}
        Return only a number between 0 and 1.
    """

    judge = completion(
        model='gpt-4o-mini',
        messages=[{
            "role": "user",
            "content": eval_prompt
        }]
    )

    score = float(judge['choices'][0]['message']['content'])

    trace.score(name="llm-as-a-judge", value=score)

except Exception as e:
    trace.error(name="completion_error", error=str(e))
    raise
