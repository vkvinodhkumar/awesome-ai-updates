import os
import time
from google import genai

# Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Models to try in order
MODELS = [
    # Latest Preview
    "gemini-3-flash-preview",

    # Stable Flash
    "gemini-3.5-flash",

    # Lite Models
    "gemini-3.1-flash-lite",

    # Gemini 2.5 Models
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.5-pro",

    # Aliases
    "gemini-flash-latest",
    "gemini-pro-latest",
]


def summarize_all(news):

    prompt = "# AI News Report\n\n"

    for i, article in enumerate(news, start=1):
        prompt += f"""
Article {i}

Title:
{article['title']}

Summary:
{article['summary']}

Link:
{article['link']}

----------------------------------------
"""

    prompt += """

Create a professional markdown report.

Include the following sections exactly:

# Executive Summary

Summarize the overall AI news.

# Article Summaries

For every article include:

- Summary
- Why it Matters

# Executive Meeting Brief

Include:

- Key Developments
- Risks
- Opportunities
- Recommended Actions

# Technology Trends

Summarize important emerging trends.

# Terminology

Explain every new AI term in simple language.
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

                print(f"SUCCESS using {model}")

                return response.text

            except Exception as e:

                last_error = e
                error = str(e)

                print(f"{model} failed")
                print(error)

                # Retry if quota/rate limit
                if (
                    "429" in error
                    or "RESOURCE_EXHAUSTED" in error
                    or "quota" in error.lower()
                ):
                    print("Quota reached.")
                    print("Waiting 10 seconds...")
                    time.sleep(10)
                    continue

                # Try next model
                break

    print("\nAll Gemini models failed.")
    print("Generating fallback report...")

    report = "# AI News Report\n\n"

    report += "## Executive Summary\n\n"
    report += (
        "Gemini API was unavailable. "
        "Displaying collected AI news without AI analysis.\n\n"
    )

    report += "## Article Summaries\n\n"

    for article in news:

        report += f"### {article['title']}\n\n"
        report += f"{article['summary']}\n\n"
        report += f"Source: {article['link']}\n\n"

    report += "## Executive Meeting Brief\n\n"
    report += "- AI analysis unavailable.\n\n"

    report += "## Technology Trends\n\n"
    report += "- Unable to generate trends.\n\n"

    report += "## Terminology\n\n"
    report += "- Unable to generate terminology.\n"

    return report