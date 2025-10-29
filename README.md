# LiteLLM + Langfuse Learning Project

This project demonstrates how to use `litellm` to interact with different large language models (LLMs) like Cohere and OpenAI, and how to use `langfuse` for tracing and observability.

## Features

- **LiteLLM Integration:** Shows how to use `litellm` to call different LLM providers with a unified interface.
- **Cohere Demo:** A script (`cohere_demo.py`) that takes a user query, gets a response from Cohere's Command R+ model, and logs the interaction to Langfuse. It also includes an example of using an LLM-as-a-judge to evaluate the model's response.
- **OpenAI Demo:** A script (`openai_demo.py`) that demonstrates a simple interaction with OpenAI's GPT-4o model.
- **Langfuse Integration:** Both demo scripts are integrated with Langfuse to trace the LLM calls, providing insights into performance and data.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- An account with Cohere, OpenAI, and Langfuse to get the necessary API keys.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kevit-devansh-rajani/litellm_langfuse_integration.git
   cd litellm-learning
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the root of the project and add your API keys:
   ```
   LANGFUSE_PUBLIC_KEY="your-langfuse-public-key"
   LANGFUSE_SECRET_KEY="your-langfuse-secret-key"
   OPENAI_API_KEY="your-openai-api-key"
   COHERE_API_KEY="your-cohere-api-key"
   ```

### Usage

- **To run the Cohere demo:**
  ```bash
  python cohere_demo.py
  ```

- **To run the OpenAI demo:**
  ```bash
  python openai_demo.py
  ```

## Project Structure

```
.
├── cohere_demo.py      # Demo script for Cohere and Langfuse
├── openai_demo.py      # Demo script for OpenAI
├── requirements.txt    # Project dependencies
├── pyproject.toml      # Project metadata
└── README.md           # This file
```

## Dependencies

This project uses the following major libraries:

- `litellm`: A library for calling LLMs using a consistent API.
- `langfuse`: An open-source platform for LLM tracing and analytics.
- `cohere`: The official Python client for the Cohere API.
- `python-dotenv`: For managing environment variables.

For a full list of dependencies, see `requirements.txt`.
