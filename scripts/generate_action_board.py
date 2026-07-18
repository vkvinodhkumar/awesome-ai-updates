def generate_action_board(report):
    """
    Extract the Recommended Actions section from the AI report.
    """

    marker = "### Recommended Actions"

    if marker in report:

        # Get everything after the marker
        action_board = report.split(marker, 1)[1]

        # Stop before the next section if it exists
        next_marker = "---"

        if next_marker in action_board:
            action_board = action_board.split(next_marker, 1)[0]

        return action_board.strip()

    return "No Recommended Actions found."