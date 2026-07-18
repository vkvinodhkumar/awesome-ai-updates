def save_index(content):

    with open("INDEX.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("INDEX.md updated.")