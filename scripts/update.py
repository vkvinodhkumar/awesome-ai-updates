from fetch_news import fetch_news
from generate_report import generate_report
from save_report import save_report

from generate_index import generate_index
from save_index import save_index


def main():
    # Fetch latest AI news
    print("Fetching AI news...")
    news = fetch_news()
    print(f"Fetched {len(news)} articles.")

    # Generate AI report
    print("Generating report...")
    report = generate_report(news)

    # Save report
    save_report(report)

    # Generate index
    print("Generating INDEX...")
    index = generate_index()

    # Save index
    save_index(index)

    print("Done!")


if __name__ == "__main__":
    main()