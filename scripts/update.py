from fetch_news import fetch_news
from generate_report import generate_report
from save_report import save_report

print("Fetching AI news...")

news = fetch_news()

print(f"Fetched {len(news)} articles.")

print("Generating report...")

report = generate_report(news)

save_report(report)

print("Done!")