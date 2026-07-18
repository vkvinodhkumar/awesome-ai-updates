from fetch_news import fetch_news
from generate_report import generate_report
from save_report import save_report

from generate_index import generate_index
from save_index import save_index

from generate_meeting_brief import generate_meeting_brief
from save_meeting_brief import save_meeting_brief

from generate_action_board import generate_action_board
from save_action_board import save_action_board

from generate_terminology import generate_terminology
from save_terminology import save_terminology


def main():

    # ------------------------------------------
    # Fetch latest AI news
    # ------------------------------------------
    print("Fetching AI news...")
    news = fetch_news()

    print(f"Fetched {len(news)} articles.")

    # ------------------------------------------
    # Generate AI report
    # ------------------------------------------
    print("Generating report...")
    report = generate_report(news)

    # ------------------------------------------
    # Save report
    # ------------------------------------------
    print("Saving report...")
    save_report(report)

    # ------------------------------------------
    # Generate INDEX
    # ------------------------------------------
    print("Generating INDEX...")
    index = generate_index()

    print("Saving INDEX...")
    save_index(index)

    # ------------------------------------------
    # Meeting Brief
    # ------------------------------------------
    print("Generating Meeting Brief...")
    meeting_brief = generate_meeting_brief(report)

    print("Saving Meeting Brief...")
    save_meeting_brief(meeting_brief)

    # ------------------------------------------
    # Action Board
    # ------------------------------------------
    print("Generating Action Board...")
    action_board = generate_action_board(report)

    print("Saving Action Board...")
    save_action_board(action_board)

    # ------------------------------------------
    # Terminology
    # ------------------------------------------
    print("Generating Terminology...")
    terminology = generate_terminology(report)

    print("Saving Terminology...")
    save_terminology(terminology)

    print("\nProject updated successfully!")


if __name__ == "__main__":
    main()