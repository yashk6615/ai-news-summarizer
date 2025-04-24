# quality_checker_openrouter.py

import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def verify_summary_with_openrouter(article, summary):
    prompt = f"""
You are an AI assistant that evaluates news summaries.

ARTICLE:
{article['content']}

SUMMARY:
{summary}

TASK:
Check if the summary is accurate, relevant, and sufficiently detailed. 
Respond with either:
- "✅ Looks good." 
- OR a short explanation of what is missing and how to improve it.
"""

    response = openai.ChatCompletion.create(
        model="deepseek/deepseek-v3-base:free",  # Or try "openai/gpt-3.5-turbo" if it's listed on OpenRouter
        messages=[
            {"role": "system", "content": "You are a strict but fair news summary evaluator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.3
    )

    return response["choices"][0]["message"]["content"].strip()
