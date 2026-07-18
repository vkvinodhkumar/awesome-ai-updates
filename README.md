# 🤖 Automated AI Updates System

An AI-powered news automation system that collects the latest AI news, summarizes it using Google's Gemini API, generates multiple Markdown reports, and automatically publishes updates using GitHub Actions.

---

# 📌 Features

- 📰 Fetches the latest AI news from multiple RSS feeds
- 🤖 Generates AI-powered summaries using Gemini
- 📄 Creates a complete AI News Report
- 📋 Generates an Executive Meeting Brief
- ✅ Generates an AI Action Board
- 📚 Generates AI Terminology
- 📑 Creates an Index of all reports
- 🕒 Stores hourly reports automatically
- ⚡ Runs automatically using GitHub Actions
- 🔄 Supports automatic model fallback
- 💾 Automatically commits generated reports to GitHub

---

# 📂 Project Structure

```text
awesome-ai-updates/
│
├── .github/
│   └── workflows/
│       └── update.yml
│
├── scripts/
│   ├── fetch_news.py
│   ├── summarize.py
│   ├── generate_report.py
│   ├── save_report.py
│   ├── generate_index.py
│   ├── save_index.py
│   ├── generate_meeting_brief.py
│   ├── save_meeting_brief.py
│   ├── generate_action_board.py
│   ├── save_action_board.py
│   ├── generate_terminology.py
│   ├── save_terminology.py
│   └── update.py
│
├── hourly/
├── daily/
├── weekly/
├── monthly/
│
├── knowledge_base/
│
├── LATEST.md
├── INDEX.md
├── MEETING_BRIEF.md
├── ACTION_BOARD.md
├── TERMINOLOGY.md
├── report.json
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Workflow

```text
RSS Feeds
      │
      ▼
Fetch Latest AI News
      │
      ▼
Gemini AI Summarization
      │
      ▼
Generate AI Report
      │
      ├── LATEST.md
      ├── INDEX.md
      ├── MEETING_BRIEF.md
      ├── ACTION_BOARD.md
      ├── TERMINOLOGY.md
      └── Hourly Reports
      │
      ▼
GitHub Actions
      │
      ▼
Automatic Git Commit
```

---

# 🧠 Technologies Used

- Python 3.12
- Google Gemini API
- Google GenAI SDK
- Feedparser
- Requests
- GitHub Actions
- Markdown
- Git

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/vkvinodhkumar/awesome-ai-updates.git
```

Move into the project

```bash
cd awesome-ai-updates
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```text
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-3-flash-preview
```

---

# ▶️ Run the Project

```bash
python scripts/update.py
```

---

# 📄 Generated Reports

Every execution generates:

- LATEST.md
- INDEX.md
- MEETING_BRIEF.md
- ACTION_BOARD.md
- TERMINOLOGY.md
- Hourly archived reports

---

# ⚙️ GitHub Actions

The workflow automatically:

- Installs dependencies
- Fetches AI news
- Generates reports
- Updates Markdown files
- Commits changes
- Pushes to GitHub

The workflow runs:

- Every hour
- Or manually using **Run Workflow**

---

# 📊 Current Features

✅ RSS Feed Collection

✅ AI Summarization

✅ Executive Summary

✅ Meeting Brief

✅ Action Board

✅ Terminology Extraction

✅ Report Index

✅ Hourly Report Archive

✅ Automatic GitHub Updates

---

# 🔮 Future Enhancements

- Daily Reports
- Weekly Reports
- Monthly Reports
- AI Knowledge Base
- JSON Report Generation
- Streamlit Dashboard
- AI Trend Analytics
- Search Functionality

---

# 👨‍💻 Author

**Vinodh Kumar**

Data Science & Analytics Enthusiast

GitHub: https://github.com/vkvinodhkumar

---

# ⭐ Project Highlights

- End-to-end AI news automation
- Gemini-powered report generation
- Automated GitHub publishing
- Modular Python architecture
- Easy to extend with new report types
- Demonstrates Python automation, API integration, and CI/CD using GitHub Actions