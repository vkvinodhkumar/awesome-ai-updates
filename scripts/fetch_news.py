import feedparser


RSS_FEEDS = [
    "https://openai.com/news/rss.xml",
    "https://huggingface.co/blog/feed.xml",
]


def fetch_news():
    news = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for article in feed.entries[:5]:

            summary = ""

            if hasattr(article, "summary"):
                summary = article.summary
            elif hasattr(article, "description"):
                summary = article.description
            else:
                summary = "No summary available."

            news.append({
                "title": article.title,
                "summary": summary,
                "link": article.link,
            })

    return news


if __name__ == "__main__":

    articles = fetch_news()

    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(article["summary"][:100])
        print(article["link"])
        print("-" * 80)