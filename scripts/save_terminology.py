from datetime import datetime


def save_terminology(content):
    """
    Save the extracted terminology.
    """

    with open("TERMINOLOGY.md", "w", encoding="utf-8") as f:

        f.write("# AI Terminology\n\n")

        f.write(
            f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        f.write(content)

    print("TERMINOLOGY.md updated.")