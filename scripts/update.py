from fetch_news import fetch_news
from generate_report import generate_report
from save_report import save_report


def main():
    print("=" * 50)
    print("Fetching AI News...")
    print("=" * 50)

    news = fetch_news()

    for i, article in enumerate(news, start=1):
        print(f"{i}. {article['title']}")

    report = generate_report(news)

    save_report(report)

    print("\nDone!")


if __name__ == "__main__":
    main()