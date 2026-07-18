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
            news.append({
                "title": article.title,
                "link": article.link
            })

    return news


if __name__ == "__main__":
    articles = fetch_news()

    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")