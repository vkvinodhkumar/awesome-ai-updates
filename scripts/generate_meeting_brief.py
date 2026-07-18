def generate_meeting_brief(report):
    """
    Extract the Meeting Brief section from the full report.
    """

    marker = "# Executive Meeting Brief"

    if marker in report:
        return report.split(marker, 1)[1].strip()

    return "Meeting brief not found."