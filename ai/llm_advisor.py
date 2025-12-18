import os
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client ONCE
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_student_advice(summary_text: str) -> str:
    """
    Send summarized student data to the LLM and return advice.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful student advisor. "
                        "Give concise, actionable advice based on the data."
                    )
                },
                {
                    "role": "user",
                    "content": summary_text
                }
            ],
            max_tokens=200
        )

        return response.choices[0].message.content.strip()

    except RateLimitError:
        return (
            "⚠️ AI advice is temporarily unavailable due to usage limits. "
            "Please try again later."
        )
