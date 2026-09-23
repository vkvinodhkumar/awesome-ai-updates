import os
import time

from google import genai


# ============================================================
# Gemini Configuration
# ============================================================

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set.")

client = genai.Client(api_key=API_KEY)


# Read models from environment variable
models_env = os.getenv(
    "GEMINI_MODELS",
    "gemini-3-flash-preview,gemini-3.5-flash,gemini-3.1-flash-lite,gemini-2.5-flash",
)

MODELS = [model.strip() for model in models_env.split(",") if model.strip()]


# ============================================================
# Generate AI Summary
# ============================================================

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

    # --------------------------------------------------------
    # Add news articles to prompt
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # Try Gemini models
    # --------------------------------------------------------

    last_error = None

    for model in MODELS:

        print("=" * 60)
        print(f"Trying model: {model}")
        print("=" * 60)

        # Two attempts per model
        for attempt in range(2):

            try:

                print(
                    f"Attempt {attempt + 1}/2 using {model}"
                )

                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                # Check whether Gemini returned usable text
                if not response or not response.text:

                    raise RuntimeError(
                        f"Gemini returned an empty response from {model}"
                    )

                print(f"Success using {model}")

                return response.text

            except Exception as e:

                last_error = e
                error = str(e)

                print(f"Error: {error}")

                # ------------------------------------------------
                # Quota / rate-limit error
                # ------------------------------------------------

                if (
                    "429" in error
                    or "RESOURCE_EXHAUSTED" in error
                    or "quota" in error.lower()
                    or "rate limit" in error.lower()
                ):

                    if attempt == 0:

                        print(
                            "Quota/rate limit detected."
                        )

                        print(
                            "Retrying in 10 seconds..."
                        )

                        time.sleep(10)

                        continue

                    else:

                        print(
                            f"Quota still unavailable for {model}."
                        )

                        print(
                            "Switching to next model..."
                        )

                        break

                # ------------------------------------------------
                # Other errors
                # ------------------------------------------------

                print(
                    f"Switching to next model..."
                )

                break


    # ============================================================
    # Gemini completely unavailable
    # ============================================================

    print("\n" + "=" * 60)
    print("All Gemini models failed.")
    print("Generating fallback report.")
    print("=" * 60)


    report = "# AI News Report\n\n"

    report += "## Executive Summary\n\n"

    report += (
        "Gemini API was unavailable. "
        "Displaying collected AI news without "
        "AI-generated analysis.\n\n"
    )


    # ------------------------------------------------------------
    # Article summaries
    # ------------------------------------------------------------

    report += "## Article Summaries\n\n"

    for article in news:

        report += f"### {article['title']}\n\n"

        report += article.get(
            "summary",
            "No summary available."
        )

        report += "\n\n"

        report += f"Source: {article['link']}\n\n"


    # ------------------------------------------------------------
    # Fallback sections
    # ------------------------------------------------------------

    report += "## Executive Meeting Brief\n\n"

    report += "- AI analysis unavailable.\n\n"


    report += "## Technology Trends\n\n"

    report += "- Unable to determine trends.\n\n"


    report += "## Terminology\n\n"

    report += "- Unable to generate terminology.\n"


    # ------------------------------------------------------------
    # Error information
    # ------------------------------------------------------------

    if last_error:

        report += (
            "\n\n"
            "Last Error:\n\n"
            f"{last_error}\n"
        )


    return report