from pathlib import Path
from datetime import datetime


def generate_index():
    hourly_folder = Path("hourly")

    reports = sorted(
        hourly_folder.glob("**/*.md"),
        reverse=True
    )

    md = "# AI Updates Index\n\n"

    md += f"_Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n\n"

    md += "## Reports\n\n"

    md += "| Date | Time | Report |\n"
    md += "|------|------|--------|\n"

    for report in reports:

        relative = report.as_posix()

        parts = report.parts

        year = parts[1]
        month = parts[2]
        day = parts[3]

        date = f"{year}-{month}-{day}"

        time = report.stem

        md += (
            f"| {date} | {time} | "
            f"[{report.name}]({relative}) |\n"
        )

    return md