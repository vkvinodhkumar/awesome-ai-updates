from datetime import datetime


def generate_report(news):
    now = datetime.now()

    report = f"# Latest AI Updates\n\n"
    report += f"Generated: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report += "---\n\n"

    for i, article in enumerate(news, start=1):
        report += f"## {i}. {article['title']}\n\n"
        report += f"Link: {article['link']}\n\n"

    return report