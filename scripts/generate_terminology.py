def generate_terminology(report):
    """
    Extract the Terminology section from the AI report.
    """

    marker = "## Terminology"

    if marker in report:

        terminology = report.split(marker, 1)[1]

        next_marker = "---"

        if next_marker in terminology:
            terminology = terminology.split(next_marker, 1)[0]

        return terminology.strip()

    return "No terminology found."