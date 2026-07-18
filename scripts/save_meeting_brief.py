def save_meeting_brief(content):
    with open("MEETING_BRIEF.md", "w", encoding="utf-8") as f:
        f.write("# Executive Meeting Brief\n\n")
        f.write(content)

    print("MEETING_BRIEF.md updated.")