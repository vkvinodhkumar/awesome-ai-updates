from pathlib import Path
from datetime import datetime

# Repository root (one level above the scripts folder)
ROOT_DIR = Path(__file__).resolve().parent.parent

LATEST_FILE = ROOT_DIR / "LATEST.md"
HOURLY_DIR = ROOT_DIR / "hourly"


def save_report(content):
    """
    Save the latest report and archive it in:
    hourly/YYYY/MM/DD/HH-MM.md
    """

    now = datetime.now()

    year = str(now.year)
    month = f"{now.month:02d}"
    day = f"{now.day:02d}"
    filename = f"{now.hour:02d}-{now.minute:02d}.md"

    # Create directory
    archive_dir = HOURLY_DIR / year / month / day
    archive_dir.mkdir(parents=True, exist_ok=True)

    # Archive file
    archive_file = archive_dir / filename

    # Save hourly report
    archive_file.write_text(content, encoding="utf-8")

    # Update latest report
    LATEST_FILE.write_text(content, encoding="utf-8")

    print("=" * 60)
    print("Report successfully saved")
    print(f"Latest report : {LATEST_FILE}")
    print(f"Hourly report : {archive_file}")
    print("=" * 60)