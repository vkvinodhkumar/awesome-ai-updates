import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

# ----------------------------------------------------
# Load environment variables
# ----------------------------------------------------
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# Preferred models (in order)
MODELS = [
    os.getenv("GEMINI_MODEL", "gemini-3-flash-preview"),
    "gemini-3.1-flash-lite",
    "gemini-flash-latest",
]


def summarize_all(news):
    """
    Summarize all news articles using ONE Gemini request.
    Automatically tries multiple models if one fails.
    """

    print(f"Preparing ONE request for {len(news)} articles...")

    prompt = """
You are an expert AI Research Analyst.

Analyze the following AI news articles.

Generate the report in Markdown using EXACTLY this structure.

# AI News Report

## Executive Summary

Write a concise summary of today's most important AI developments (5–8 sentences).

---

## Article Summaries

For EACH article provide:

### Title

**Summary**
Write 3–4 concise sentences.

**Why it matters**
Write 2–3 concise sentences.

---

## Executive Meeting Brief

### Key Developments
- Bullet points

### Risks
- Bullet points

### Opportunities
- Bullet points

### Recommended Actions
1. Numbered recommendations

---

## Technology Trends

List important:
- AI Models
- Companies
- Research
- Products
- Technologies

mentioned today.

---

## Terminology

List important AI terms with a one-line explanation.

---

Return ONLY valid Markdown.
"""

    for i, article in enumerate(news, start=1):
        prompt += f"""

Article {i}

Title:
{article['title']}

Source:
{article['link']}
"""

    # ----------------------------------------------------
    # Try models one by one
    # ----------------------------------------------------
    for model in MODELS:

        try:
            print(f"\nTrying model: {model}")

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            print(f"Success using {model}")

            return response.text

        except ClientError as e:
            print(f"{model} failed")
            print(e)

        except Exception as e:
            print(f"{model} failed")
            print(e)

    # ----------------------------------------------------
    # All models failed
    # ----------------------------------------------------
    print("\nGemini quota exceeded or API unavailable.")

    report = "# AI Report\n\n"

    report += "⚠️ **AI summarization is currently unavailable.**\n\n"

    report += (
        "The latest AI news was collected successfully, "
        "but Gemini could not generate summaries because "
        "all configured models were unavailable or out of quota.\n\n"
    )

    report += "---\n\n"

    report += "## Latest Headlines\n\n"

    for article in news:
        report += f"### {article['title']}\n"
        report += f"Source: {article['link']}\n\n"

    return report