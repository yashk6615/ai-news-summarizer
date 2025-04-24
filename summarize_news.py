# summarize_news.py

import os
from gpt4all import GPT4All
from fetch_news import get_news
from quality_checker_openai import verify_summary_with_openrouter




# Force model to run on CPU only (bypasses CUDA errors)
os.environ["LLAMA_CPP_FORCE_CPU"] = "1"

# Initialize model
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf", model_path="C:/Users/PC/AppData/Local/nomic.ai/GPT4All")

def summarize_article(article):
    prompt = f"Briefly explain (as if you are the writer of article) the following news article in 5 main points covering the main events, outcome and involved parties:\n\n{article['content']}\n\nSummary:"
    return model.generate(prompt, max_tokens=600)

if __name__ == "__main__":
    news = get_news()

    print(f"\n📡 Total articles fetched: {len(news)}")

    if not news:
        print("❌ No news articles returned. Check your API key or query.")
    else:
        for article in news:
            print(f"\n📰 Title: {article['title']}")
            print(f"🔗 URL: {article['url']}")
            print("📌 Summary:")
            summary = summarize_article(article)
            print(summary)
            # Run quality checker
            print("🧠 Deepseek Quality Feedback:")
            if not summary or len(summary.split()) < 5:
                feedback = "❌ Summary too short or missing."
            else:
                feedback = verify_summary_with_openrouter(article, summary)
                if not feedback.strip():
                    feedback = "⚠️ No feedback returned. Please review manually."
                print(feedback)
            