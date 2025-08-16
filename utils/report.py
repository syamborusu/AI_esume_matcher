import os
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None


def generate_suggestions_with_openai(resume_text: str, jd_text: str) -> str:
    """Uses OpenAI ChatCompletion to generate strengths, gaps, and suggestions."""
    if client is None:
        return (
            "OpenAI API key not set. Set OPENAI_API_KEY environment variable to enable AI suggestions."
        )

    prompt = f"""
You are an assistant that compares a candidate resume to a job description.
Provide:
1) Short summary (1-2 lines)
2) Top strengths found in the resume (bullet points)
3) Missing skills / gaps relative to the job description (bullet points)
4) Concrete suggestions to improve the resume (5 bullets)

Resume:
{resume_text[:3000]}

Job Description:
{jd_text[:3000]}

Respond in clear bullet points.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # change to available model if needed
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
    )
    return response.choices[0].message.content


def generate_report(resume_text: str, jd_text: str, score: float, top_resume_keywords=None, top_jd_keywords=None) -> str:
    report = []
    report.append(f"Match Score: {score}%")
    report.append("\nTop Resume Keywords: " + ", ".join(top_resume_keywords or []))
    report.append("\nTop JD Keywords: " + ", ".join(top_jd_keywords or []))
    report.append("\n\nAI Suggestions:\n")
    ai_section = generate_suggestions_with_openai(resume_text, jd_text)
    report.append(ai_section)
    return "\n".join(report)