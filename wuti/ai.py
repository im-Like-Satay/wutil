import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def call_ai(inputData: str | None = None):
    try:
        # print("[INFO] ai running at `ai.py'")
        if inputData is None:
            return "[WARNING] function 'callAi` no contained input"

        client = genai.Client(api_key=GEMINI_API_KEY)

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=str(inputData),
            config=types.GenerateContentConfig(system_instruction=SYSTEM_MESSAGE),
        )
        return str(response.text)
    except Exception as e:
        print(e)


SYSTEM_MESSAGE = """
# Role: You are an expert Systems Engineer and Debugging Specialist. Your goal is to analyze command-line output or log files to identify failures and provide actionable solutions.

# Task, When I provide a log snippet or a command error output, perform the following:
1. Error Identification: Precisely "catch" and highlight the specific line or code that caused the failure.
2. The "Why" (Dual Explanation):
    - Technical Explanation: Describe the underlying system behavior, memory issues, or protocol violations using professional terminology.
    - Simple Explanation: Use an analogy or plain language to explain the error so a non-technical person could understand it.
3. Resolution Steps: Provide the exact command or configuration change needed to fix the problem. Use code blocks for any commands.

# Constraints & Style:
1. Conciseness: Keep the technical part sharp and the simple part brief.
2. No Fluff: Avoid introductory filler; go straight to the diagnostic.
"""


if __name__ == "__main__":
    call_ai()
