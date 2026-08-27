# 🤖 Automated AI Updates System

An AI-powered news automation system that collects the latest AI news from multiple RSS feeds, summarizes it using Google's Gemini API, generates structured Markdown reports, and automatically publishes updates using GitHub Actions.

The system is designed to provide AI information in different formats for **managers, executives, business professionals, data scientists, students, researchers, developers, and general readers**.

---

# 📌 Features

- 📰 Fetches the latest AI news from multiple RSS feeds
- 🤖 Generates AI-powered summaries using Google Gemini
- 📄 Creates a complete AI News Report
- 📋 Generates an Executive Meeting Brief
- ✅ Generates an AI Action Board
- 📚 Generates AI Terminology
- 📑 Creates an Index of reports
- 🕒 Stores hourly reports automatically
- ⚡ Runs automatically using GitHub Actions
- 🔄 Supports automatic Gemini model fallback
- 💾 Automatically commits generated reports to GitHub
- 📊 Provides different reports for different audiences

---

# 👥 Who Should Read What?

This project generates different AI reports for different types of readers.

| Audience | Recommended File | Purpose |
|---|---|---|
| 👔 **Manager / Executive** | `MEETING_BRIEF.md` | Quick overview of important AI developments, business impact, and key points for decision-making |
| 📊 **Data Scientist / Data Analyst** | `LATEST.md` | Follow detailed AI news, technologies, models, research, and industry trends |
| 👨‍🎓 **Student / Learner** | `TERMINOLOGY.md` | Learn important AI concepts, technologies, and terminology |
| 💼 **Business / Product Professional** | `ACTION_BOARD.md` | Identify AI opportunities, implications, and areas requiring action |
| 🔬 **Researcher** | `INDEX.md` + `hourly/` | Explore historical AI developments and track how AI topics evolve |
| 👨‍💻 **Developer** | `scripts/` | Understand the Python implementation, AI integration, report generation, and data flow |
| ⚙️ **DevOps / Automation Engineer** | `.github/workflows/update.yml` | Understand GitHub Actions scheduling, execution, automation, and publishing |
| 🧠 **AI / ML Enthusiast** | `LATEST.md` + `TERMINOLOGY.md` | Follow current AI developments while learning the concepts behind them |
| 🌐 **General Reader** | `LATEST.md` | Quickly understand the most important current AI developments |
| 🗂️ **Project Maintainer** | `scripts/update.py` | Understand the complete application pipeline and how all components work together |

---

# 🎯 Quick Starting Guide

## 👔 Manager / Executive

Start with:

`MEETING_BRIEF.md`

Best for:

- Major AI developments
- Business impact
- Important industry changes
- Key points requiring attention
- Decision-making

---

## 📊 Data Scientist / Data Analyst

Start with:

`LATEST.md`

Then explore:

`INDEX.md`

Best for:

- AI trends
- New AI technologies
- Model releases
- Research developments
- Industry developments

---

## 👨‍🎓 Student / Learner

Start with:

`TERMINOLOGY.md`

Then read:

`LATEST.md`

Best for:

- AI terminology
- New technologies
- Machine learning concepts
- Generative AI
- Industry vocabulary

---

## 💼 Business / Product Professional

Start with:

`ACTION_BOARD.md`

Then:

`MEETING_BRIEF.md`

Best for:

- AI opportunities
- Business implications
- Important developments
- Potential actions
- Product opportunities

---

## 🔬 Researcher

Start with:

`INDEX.md`

Then explore:

`hourly/`

Best for:

- Historical AI developments
- Research announcements
- Technology evolution
- Tracking AI trends over time

---

## 👨‍💻 Developer

Start with:

`scripts/update.py`

Then explore:

`scripts/`

Best for understanding:

- Python architecture
- RSS data collection
- Gemini API integration
- AI summarization
- Report generation
- File generation
- Automation pipeline

---

## ⚙️ DevOps / Automation Engineer

Start with:

`.github/workflows/update.yml`

Best for understanding:

- GitHub Actions
- Scheduled execution
- Python environment setup
- Dependency installation
- Automated execution
- Git commits
- Automatic publishing

---

## 🧠 AI / ML Enthusiast

Recommended reading order:

`LATEST.md` → `TERMINOLOGY.md` → `ACTION_BOARD.md` → `INDEX.md`

This provides:

**Current News → AI Concepts → Practical Opportunities → Historical Information**

---

## 🌐 General Reader

Start with:

`LATEST.md`

This is the easiest way to understand the latest important developments in AI.

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
│   ├── test_gemini.py
│   └── update.py
│
├── hourly/
│
├── LATEST.md
├── INDEX.md
├── MEETING_BRIEF.md
├── ACTION_BOARD.md
├── TERMINOLOGY.md
├── reports.json
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Workflow

```text
                    RSS FEEDS
                       │
                       ▼
               Fetch Latest AI News
                       │
                       ▼
                Gemini AI Processing
                       │
                       ▼
                 AI Summarization
                       │
                       ▼
                 Generate AI Report
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
     LATEST.md    MEETING_BRIEF   ACTION_BOARD
          │            │            │
          └────────────┼────────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       TERMINOLOGY.md        INDEX.md
             │                   │
             └─────────┬─────────┘
                       ▼
                 Hourly Reports
                       │
                       ▼
                GitHub Actions
                       │
                       ▼
                 Git Commit
                       │
                       ▼
                GitHub Repository
```

---

# 🧠 Main Application Pipeline

The main controller is:

`scripts/update.py`

It coordinates the complete system.

```text
Fetch News
    ↓
Generate Report
    ↓
Save Report
    ↓
Generate Index
    ↓
Save Index
    ↓
Generate Meeting Brief
    ↓
Save Meeting Brief
    ↓
Generate Action Board
    ↓
Save Action Board
    ↓
Generate Terminology
    ↓
Save Terminology
```

---

# 📰 News Collection

The system collects AI news from configured RSS feeds.

Main file:

`scripts/fetch_news.py`

Pipeline:

```text
RSS Feeds
    ↓
fetch_news.py
    ↓
Latest AI Articles
```

---

# 🤖 AI Summarization

The collected news is processed using Google's Gemini API.

Main file:

`scripts/summarize.py`

Pipeline:

```text
AI News
   ↓
Gemini API
   ↓
AI-generated summaries
```

The project supports automatic model fallback so that alternative configured Gemini models can be used when required.

---

# 📄 Generated Reports

The system generates several different reports for different audiences.

## LATEST.md

Contains the latest AI news and generated summaries.

**Recommended for:**

- Data Scientists
- Data Analysts
- AI/ML Enthusiasts
- General Readers

---

## MEETING_BRIEF.md

Provides an executive-oriented summary of important AI developments.

**Recommended for:**

- Managers
- Executives
- Team Leads
- Business Professionals

---

## ACTION_BOARD.md

Converts AI developments into action-oriented insights.

**Recommended for:**

- Product Professionals
- Business Professionals
- Managers
- AI Strategy Teams

---

## TERMINOLOGY.md

Contains important AI terminology and concepts extracted from the generated reports.

**Recommended for:**

- Students
- Beginners
- AI/ML Learners
- Developers learning AI

---

## INDEX.md

Provides an index of generated reports and historical information.

**Recommended for:**

- Researchers
- Analysts
- Project Maintainers

---

## hourly/

Contains archived hourly AI reports.

**Recommended for:**

- Researchers
- Analysts
- Anyone interested in historical AI developments

---

# 🐍 Python Scripts

The `scripts/` directory contains the core implementation.

### `fetch_news.py`

Collects AI news from RSS feeds.

### `summarize.py`

Uses Gemini to summarize AI news.

### `generate_report.py`

Generates the main AI report.

### `save_report.py`

Saves generated reports.

### `generate_index.py`

Generates the report index.

### `save_index.py`

Saves the generated index.

### `generate_meeting_brief.py`

Generates the executive meeting brief.

### `save_meeting_brief.py`

Saves the meeting brief.

### `generate_action_board.py`

Generates the AI action board.

### `save_action_board.py`

Saves the action board.

### `generate_terminology.py`

Generates AI terminology.

### `save_terminology.py`

Saves the terminology report.

### `test_gemini.py`

Used to test Gemini API functionality.

### `update.py`

Main controller that executes the complete pipeline.

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

## Clone the Repository

```bash
git clone https://github.com/vkvinodhkumar/awesome-ai-updates.git
```

## Move into the Project

```bash
cd awesome-ai-updates
```

## Install Dependencies

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

For GitHub Actions, store the Gemini API key as a GitHub Actions Secret.

**Never commit API keys or other secrets to the repository.**

---

# ▶️ Run the Project

Run the complete pipeline:

```bash
python scripts/update.py
```

The system will:

```text
Fetch AI News
      ↓
Summarize News
      ↓
Generate AI Report
      ↓
Generate Index
      ↓
Generate Meeting Brief
      ↓
Generate Action Board
      ↓
Generate Terminology
      ↓
Save Reports
```

---

# 📄 Generated Outputs

Every successful execution can update:

```text
LATEST.md
INDEX.md
MEETING_BRIEF.md
ACTION_BOARD.md
TERMINOLOGY.md
reports.json
hourly/
```

---

# ⚙️ GitHub Actions

The workflow is located at:

`.github/workflows/update.yml`

GitHub Actions automatically:

- Installs dependencies
- Sets up Python
- Fetches AI news
- Runs the AI processing pipeline
- Generates reports
- Updates Markdown files
- Creates Git commits
- Pushes changes to GitHub

---

# ⏰ Automatic Schedule

The workflow is configured to run automatically every hour.

```yaml
schedule:
  - cron: "0 * * * *"
```

This means:

```text
Every hour
at minute 00
UTC
```

The workflow can also be executed manually using:

```text
GitHub
   ↓
Actions
   ↓
Automated AI Updates
   ↓
Run workflow
```

---

# 📊 Current Features

✅ RSS Feed Collection

✅ AI News Summarization

✅ Gemini API Integration

✅ AI News Report

✅ Executive Meeting Brief

✅ AI Action Board

✅ AI Terminology

✅ Report Index

✅ Hourly Report Archive

✅ Automatic GitHub Updates

✅ Scheduled GitHub Actions

✅ Automatic Git Commit and Push

✅ Gemini Model Fallback

---

# 🔮 Future Enhancements

- 📅 Daily Reports
- 📆 Weekly Reports
- 🗓️ Monthly Reports
- 🧠 AI Knowledge Base
- 📊 Advanced JSON Reporting
- 📈 AI Trend Analytics
- 🔎 Search Functionality
- 📊 Streamlit Dashboard
- 📈 Historical AI Trend Analysis
- 🏷️ AI Topic Classification
- 🔍 Advanced Report Search

---

# ⭐ Project Highlights

- End-to-end AI news automation
- RSS-based AI news collection
- Gemini-powered summarization
- Automated report generation
- Executive-focused reporting
- Action-oriented AI insights
- AI terminology extraction
- Historical hourly reports
- Automated GitHub publishing
- Scheduled GitHub Actions
- Modular Python architecture
- API integration
- CI/CD automation
- Easy to extend with new report types

---

# 👨‍💻 Author

**Vinodh Kumar**

Data Science & Analytics Enthusiast

GitHub: https://github.com/vkvinodhkumar
