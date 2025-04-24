# 📰 AI News Summarizer & Quality Evaluator

An intelligent app that fetches top headlines by topic and country, generates summaries using a local LLM (GPT4All), and evaluates their quality using DeepSeek via OpenRouter.

---

## 🚀 Features

- ✅ Fetch top headlines using GNews API
- ✅ Summarize articles with GPT4All (offline local model)
- ✅ Evaluate summary quality with DeepSeek
- ✅ Simple UI built with Streamlit
- ✅ Secure API keys using `.env`

---

## 📦 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **LLM**: GPT4All (orca-mini-3b)
- **Quality Checker**: DeepSeek via OpenRouter
- **News API**: GNews API
- **Secrets Management**: Python-dotenv

---

## 🛠️ Setup Instructions

1. **Install dependencies**:

pip install -r requirements.txt

## Create your .env file and add this 
GNEWS_API_KEY=your_gnews_key
OPENROUTER_API_KEY=your_openrouter_key

## Installation of local llm 

1. Download GPT4All desktop app
2. Go to Models Section
3. Select a Model depending upon your system specs
4. give the model path of that model in your files (news_summarizer.py,app.py)


## Screenshots

![main_section](https://github.com/user-attachments/assets/5d34ccda-58fc-4bb3-bc3f-d7a67d7b602c)


![summary_news](https://github.com/user-attachments/assets/fa08722f-f19d-43ca-a1d1-6780dd8b08f8)

