from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo


# Repository root
ROOT_DIR = Path(__file__).resolve().parent.parent

# Output locations
HOURLY_DIR = ROOT_DIR / "hourly"
LATEST_FILE = ROOT_DIR / "LATEST.md"


def save_report(content):
    """
    Save the latest AI report and archive it in:
    hourly/YYYY/MM/DD/HH-MM.md
    """

    # Use Indian Standard Time (IST)
    now = datetime.now(ZoneInfo("Asia/Kolkata"))

    year = f"{now.year}"
    month = f"{now.month:02d}"
    day = f"{now.day:02d}"

    # Create folder structure
    report_folder = HOURLY_DIR / year / month / day
    report_folder.mkdir(parents=True, exist_ok=True)

    # File name
    filename = f"{now.hour:02d}-{now.minute:02d}.md"

    # Archive report path
    report_file = report_folder / filename

    # Save archive report
    report_file.write_text(content, encoding="utf-8")

    # Update latest report
    LATEST_FILE.write_text(content, encoding="utf-8")

    print("=" * 60)
    print("AI Report Saved Successfully")
    print("=" * 60)
    print(f"Latest Report : {LATEST_FILE}")
    print(f"Archive Report: {report_file}")
    print("=" * 60)

    return report_file