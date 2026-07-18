from datetime import datetime


def save_action_board(content):
    """
    Save the extracted action board.
    """

    with open("ACTION_BOARD.md", "w", encoding="utf-8") as f:

        f.write("# AI Action Board\n\n")

        f.write(
            f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        f.write(content)

    print("ACTION_BOARD.md updated.")