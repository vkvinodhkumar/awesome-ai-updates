import os
import time
from google import genai

# Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Read models from environment variable
models_env = os.getenv(
    "GEMINI_MODELS",
    "gemini-3-flash-preview,gemini-3.5-flash,gemini-3.1-flash-lite,gemini-2.5-flash"
)

MODELS = [m.strip() for m in models_env.split(",") if m.strip()]

# Rest of your code...


def summarize_all(news):

    prompt = """
You are an AI technology analyst.

Generate a professional Markdown report.

Use the following structure exactly.

# AI News Report

## Executive Summary

Provide a concise overview of today's AI news.

## Article Summaries

For every article include:

### Article Title

Summary

Why it Matters

## Executive Meeting Brief

Include:

- Key Developments
- Risks
- Opportunities
- Recommended Actions

## Technology Trends

Summarize important trends.

## Terminology

Explain every new AI term in simple language.

-----------------------------------------

Today's Articles

"""

    for i, article in enumerate(news, start=1):

        prompt += f"""

Article {i}

Title:
{article['title']}

Summary:
{article.get("summary", "No summary available.")}

Link:
{article['link']}

-----------------------------------------
"""

    last_error = None

    for model in MODELS:

        print("=" * 60)
        print(f"Trying model: {model}")
        print("=" * 60)

        for attempt in range(2):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                print(f"Success using {model}")

                return response.text

            except Exception as e:

                last_error = e
                error = str(e)

                print(error)

                if (
                    "429" in error
                    or "RESOURCE_EXHAUSTED" in error
                    or "quota" in error.lower()
                ):
                    print("Quota reached.")
                    print("Retrying in 10 seconds...")
                    time.sleep(10)
                    continue

                print(f"Switching to next model...\n")
                break

    print("\nAll Gemini models failed.")
    print("Generating fallback report...\n")

    report = "# AI News Report\n\n"

    report += "## Executive Summary\n\n"
    report += (
        "Gemini API was unavailable. "
        "Displaying collected AI news without AI-generated analysis.\n\n"
    )

    report += "## Article Summaries\n\n"

    for article in news:

        report += f"### {article['title']}\n\n"

        report += article.get(
            "summary",
            "No summary available."
        )

        report += "\n\n"

        report += f"Source: {article['link']}\n\n"

    report += "## Executive Meeting Brief\n\n"
    report += "- AI analysis unavailable.\n\n"

    report += "## Technology Trends\n\n"
    report += "- Unable to determine trends.\n\n"

    report += "## Terminology\n\n"
    report += "- Unable to generate terminology.\n"

    if last_error:
        report += f"\n\nLast Error:\n\n{last_error}\n"

    return report