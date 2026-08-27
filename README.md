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

```text
MEETING_BRIEF.md
```

Best for:

- Major AI developments
- Business impact
- Important industry changes
- Key points requiring attention
- Decision-making

---

## 📊 Data Scientist / Data Analyst

Start with:

```text
LATEST.md
```

Then explore:

```text
INDEX.md
```

Best for:

- AI trends
- New AI technologies
- Model releases
- Research developments
- Industry developments

---

## 👨‍🎓 Student / Learner

Start with:

```text
TERMINOLOGY.md
```

Then read:

```text
LATEST.md
```

Best for:

- AI terminology
- New technologies
- Machine learning concepts
- Generative AI
- Industry vocabulary

---

## 💼 Business / Product Professional

Start with:

```text
ACTION_BOARD.md
```

Then:

```text
MEETING_BRIEF.md
```

Best for:

- AI opportunities
- Business implications
- Important developments
- Potential actions
- Product opportunities

---

## 🔬 Researcher

Start with:

```text
INDEX.md
```

Then explore:

```text
hourly/
```

Best for:

- Historical AI developments
- Research announcements
- Technology evolution
- Tracking AI trends over time

---

## 👨‍💻 Developer

Start with:

```text
scripts/update.py
```

Then explore:

```text
scripts/
```

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

```text
.github/workflows/update.yml
```

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

```text
LATEST.md
      ↓
TERMINOLOGY.md
      ↓
ACTION_BOARD.md
      ↓
INDEX.md
```

This provides:

```text
Current News
     ↓
AI Concepts
     ↓
Practical Opportunities
     ↓
Historical Information
```

---

## 🌐 General Reader

Start with:

```text
LATEST.md
```

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

```text
scripts/update.py
```

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

```text
scripts/fetch_news.py
```

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

```text
scripts/summarize.py
```

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

## `LATEST.md`

Contains the latest AI news and generated summaries.

**Recommended for:**

- Data Scientists
- Data Analysts
- AI/ML Enthusiasts
- General Readers

---

## `MEETING_BRIEF.md`

Provides an executive-oriented summary of important AI developments.

**Recommended for:**

- Managers
- Executives
- Team Leads
- Business Professionals

---

## `ACTION_BOARD.md`

Converts AI developments into action-oriented insights.

**Recommended for:**

- Product Professionals
- Business Professionals
- Managers
- AI Strategy Teams

---

## `TERMINOLOGY.md`

Contains important AI terminology and concepts extracted from the generated reports.

**Recommended for:**

- Students
- Beginners
- AI/ML Learners
- Developers learning AI

---

## `INDEX.md`

Provides an index of generated reports and historical information.

**Recommended for:**

- Researchers
- Analysts
- Project Maintainers

---

## `hourly/`

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

# 🚀 How to Use

There are two main ways to use this project:

1. 📖 Read the generated AI reports
2. ⚙️ Run the AI news automation system

---

## 📖 1. Read the Generated Reports

You do **not** need to install anything if you only want to read the reports.

Choose the file based on your requirement:

| If you are a... | Read | What you get |
|---|---|---|
| 👔 Manager / Executive | `MEETING_BRIEF.md` | Executive-level AI updates and business insights |
| 📊 Data Scientist / Analyst | `LATEST.md` | Latest AI news, technologies, models, and trends |
| 👨‍🎓 Student / Learner | `TERMINOLOGY.md` | AI concepts, terminology, and technologies |
| 💼 Business / Product Professional | `ACTION_BOARD.md` | AI opportunities, implications, and actions |
| 🔬 Researcher | `INDEX.md` + `hourly/` | Historical AI developments and archived reports |
| 👨‍💻 Developer | `scripts/` | Source code and implementation |
| ⚙️ DevOps Engineer | `.github/workflows/update.yml` | Automation and scheduled workflow |
| 🌐 General Reader | `LATEST.md` | Quick overview of current AI developments |

---

## ▶️ 2. Run the Project Locally

### Step 1 — Clone the Repository

```bash
git clone https://github.com/vkvinodhkumar/awesome-ai-updates.git
```

### Step 2 — Enter the Project Directory

```bash
cd awesome-ai-updates
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure Gemini API

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-3-flash-preview
```

Replace `YOUR_API_KEY` with your actual Gemini API key.

**Never commit the `.env` file or API key to GitHub.**

### Step 5 — Run the Automation

Execute:

```bash
python scripts/update.py
```

The program will automatically:

```text
Fetch AI News
      ↓
Process News
      ↓
Generate AI Summaries
      ↓
Generate AI Report
      ↓
Generate INDEX
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

# ⚙️ GitHub Actions Automation

You can also allow GitHub Actions to run the project automatically.

The workflow is located at:

```text
.github/workflows/update.yml
```

The workflow performs:

```text
GitHub Actions
      ↓
Setup Python
      ↓
Install Dependencies
      ↓
Run scripts/update.py
      ↓
Generate Reports
      ↓
Commit Changes
      ↓
Push Changes
```

---

## 🔑 Configure GitHub Secret

For GitHub Actions, the Gemini API key should be stored as a repository secret.

Go to:

```text
GitHub Repository
      ↓
Settings
      ↓
Secrets and variables
      ↓
Actions
      ↓
New repository secret
```

Create:

```text
Name:
GEMINI_API_KEY

Value:
YOUR_GEMINI_API_KEY
```

The workflow reads the secret using:

```yaml
env:
  GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
```

---

# ⏰ Automatic Updates

The GitHub Actions workflow is scheduled to run every hour.

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

The workflow can also be started manually.

Go to:

```text
Actions
   ↓
Automated AI Updates
   ↓
Run workflow
```

---

# 📄 Where to Find the Results

After the automation completes, generated files are available in the repository:

```text
LATEST.md
INDEX.md
MEETING_BRIEF.md
ACTION_BOARD.md
TERMINOLOGY.md
reports.json
hourly/
```

### Latest AI Updates

```text
LATEST.md
```

### Executive Summary

```text
MEETING_BRIEF.md
```

### Actionable Insights

```text
ACTION_BOARD.md
```

### AI Terminology

```text
TERMINOLOGY.md
```

### Historical Reports

```text
hourly/
```

### Report Index

```text
INDEX.md
```

---

# 🔄 Typical Usage

A normal automated execution looks like this:

```text
        New AI News
             ↓
        RSS Feeds
             ↓
       fetch_news.py
             ↓
        Gemini API
             ↓
       AI Summaries
             ↓
     generate_report.py
             ↓
      ┌──────┼──────┐
      ↓      ↓      ↓
   Latest  Meeting  Action
    News    Brief   Board
      │       │       │
      └───────┼───────┘
              ↓
        Terminology
              ↓
           INDEX
              ↓
       Hourly Archive
              ↓
        GitHub Commit
```

---

# 🛠️ Manual Development Usage

If you are modifying the project, you can run individual components for testing.

### Test Gemini

```bash
python scripts/test_gemini.py
```

### Run the complete pipeline

```bash
python scripts/update.py
```

The recommended approach is:

```bash
python scripts/update.py
```

because it runs the complete pipeline.

---

# 🧭 Recommended Usage by User Type

### 👔 Manager

```text
MEETING_BRIEF.md
```

Read this when you need a quick understanding of major AI developments and their potential business relevance.

### 📊 Data Scientist

```text
LATEST.md
INDEX.md
```

Use these to follow AI technologies, models, research, and industry trends.

### 👨‍🎓 Student

```text
TERMINOLOGY.md
LATEST.md
```

Use these to learn AI terminology while following current developments.

### 💼 Business / Product

```text
ACTION_BOARD.md
MEETING_BRIEF.md
```

Use these to identify opportunities and potential actions related to AI developments.

### 🔬 Researcher

```text
INDEX.md
hourly/
```

Use these to explore historical reports and track AI developments over time.

### 👨‍💻 Developer

```text
scripts/
scripts/update.py
```

Use these to understand and modify the automation pipeline.

### ⚙️ DevOps Engineer

```text
.github/workflows/update.yml
```

Use this to understand and manage GitHub Actions automation.

---

# 🚦 Simplest Way to Use the Project

If you are only interested in **AI news**:

```text
Open → LATEST.md
```

If you are a **manager**:

```text
Open → MEETING_BRIEF.md
```

If you are a **student**:

```text
Open → TERMINOLOGY.md
```

If you want **business actions**:

```text
Open → ACTION_BOARD.md
```

If you want **historical information**:

```text
Open → INDEX.md
```

If you want to **run the system yourself**:

```bash
python scripts/update.py
```

If you want **automatic hourly updates**:

```text
Configure GEMINI_API_KEY
        ↓
Enable GitHub Actions
        ↓
Workflow runs automatically
```

---

# 🗺️ Complete Usage Flow

```text
Clone Repository
       ↓
Install Dependencies
       ↓
Configure Gemini API
       ↓
Run update.py
       ↓
Fetch AI News
       ↓
Generate AI Reports
       ↓
Read Generated Reports
       ↓
Configure GitHub Secret
       ↓
Enable GitHub Actions
       ↓
Automatic Hourly Updates
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
