from datetime import datetime
from summarize import summarize_all


def generate_report(news):
    print("Sending all articles to Gemini...")

    summary = summarize_all(news)

    report = f"# Latest AI Updates\n\n"

    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    report += "---\n\n"

    report += summary

    return report