import streamlit as st
from fetch_news import get_news
from summarize_news import summarize_article
from quality_checker_openai import verify_summary_with_openrouter

# Set up Streamlit page configuration
st.set_page_config(page_title="News Summarizer & Quality Evaluator", layout="wide")
st.title("📰 News Summarizer & Quality Evaluator")

# User inputs for news topic, country, and number of articles
topic = st.text_input("Enter topic (e.g., 'Business', 'Politics', 'Technology')", "Business")
country = st.text_input("Enter country code (e.g., 'us', 'in', 'gb')", "us")
max_articles = st.number_input("Enter number of articles to fetch", min_value=1, max_value=20, value=3)

# Button to trigger fetching and summarizing the news
if st.button("📡 Fetch and Summarize Latest News"):
    # Fetch news articles based on the user inputs
    news_articles = get_news(query=topic, country=country, max_articles=max_articles)

    # Check if any articles are fetched
    if not news_articles:
        st.error("❌ No articles found. Please check your topic and country codes.")
    else:
        st.success(f"📄 Fetched {len(news_articles)} articles.")
        # Iterate through each fetched article and process
        for article in news_articles:
            title = article.get("title", "Untitled")
            url = article.get("url", "#")
            content = article.get("content", "")

            st.subheader(f"📌 {title}")
            st.markdown(f"🔗 [Read Full Article]({url})")

            # Check if content is available and valid
            if not content or len(content.split()) < 20:
                st.warning("⚠️ Article content is too short or missing.")
                continue

            # Summarize the article
            with st.spinner("🔍 Generating summary..."):
                summary = summarize_article(article)

            # Display the summary
            st.markdown(f"**📝 Summary:** {summary}")

            # Evaluate the summary quality
            with st.spinner("🧠 Evaluating summary quality..."):
                try:
                    article["summary"] = summary  # Add summary to the article
                    feedback = verify_summary_with_openrouter(article, summary)
                except Exception as e:
                    feedback = f"❌ Error during quality check: {str(e)}"

            # Display the feedback for quality
            st.markdown(f"**✅ Quality Feedback:** {feedback}")
            st.markdown("---")
