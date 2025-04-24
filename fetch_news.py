# fetch_news.py

import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GNEWS_API_KEY")

def get_news(query="Business", country="us", max_articles=3):
    if not api_key:
        raise ValueError("GNEWS_API_KEY is missing in your .env file")

    url = (
        f"https://gnews.io/api/v4/search?"
        f"q={query}&"
        f"lang=en&"
        f"country={country}&"
        f"max={max_articles}&"
        f"token={api_key}"
    )

    response = requests.get(url)
    data = response.json()

    articles = []
    for article in data.get("articles", []):
        if article.get("content"):  # Only include articles with content
            articles.append({
                "title": article["title"],
                "content": article["content"],
                "url": article["url"]
            })

    return articles
