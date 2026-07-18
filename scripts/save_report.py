from pathlib import Path
from datetime import datetime


def save_report(content):
    now = datetime.now()

    year = str(now.year)
    month = f"{now.month:02d}"
    day = f"{now.day:02d}"

    folder = Path("hourly") / year / month / day
    folder.mkdir(parents=True, exist_ok=True)

    filename = f"{now.hour:02d}-{now.minute:02d}.md"

    filepath = folder / filename

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    with open("LATEST.md", "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Report saved to: {filepath}")
    print("LATEST.md updated.")