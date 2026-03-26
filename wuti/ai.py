import os
from enum import Enum

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


class Provider(Enum):
    groq = "groq"
    gemini = "gemini"
    openai = "openai"
    anthropic = "anthropic"


PROVIDER = os.getenv("PROVIDER")
PROVIDER = Provider(PROVIDER)


def call_ai(inputData: str | None = None, temperature: float = 0.1):
    # set model for each provider
    if PROVIDER == Provider.groq:
        llm = ChatGroq(
            model="groq/compound", api_key=GROQ_API_KEY, temperature=temperature
        )
    elif PROVIDER == Provider.gemini:
        llm = ChatGoogleGenerativeAI(
            model="gemini-3-flash", api_key=GEMINI_API_KEY, temperature=temperature
        )
    elif PROVIDER == Provider.openai:
        llm = ChatOpenAI(
            model="gpt-5.4", api_key=OPENAI_API_KEY, temperature=temperature
        )
    elif PROVIDER == Provider.anthropic:
        llm = ChatAnthropic(
            model="claude-sonnet-4-6", api_key=ANTROPIC_API_KEY, temperature=temperature
        )

    if inputData is None:
        return "[WARNING] function 'callAi` no contained input"

    return llm.invoke([SystemMessage(SYSTEM_MESSAGE), HumanMessage(str(inputData))]).content


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
    print(call_ai())
