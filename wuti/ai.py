import os
from dotenv import load_dotenv
from enum import Enum

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

class Provider(Enum):
    groq = 'groq'
    gemini = 'gemini'
    openai = 'openai'
    anthropic = 'anthropic'

PROVIDER = os.getenv("PROVIDER")
PROVIDER = Provider(PROVIDER)

def callAi(inputData: str | None = None, temperature: float = 0.1):
    # set model for each provider
    if PROVIDER == Provider.groq:
        llm = ChatGroq(model="groq/compound", api_key=GROQ_API_KEY, temperature=temperature)
    elif PROVIDER == Provider.gemini:
        llm = ChatGoogleGenerativeAI(model="gemini-3-flash", api_key=GEMINI_API_KEY, temperature=temperature)
    elif PROVIDER == Provider.openai:
        llm = ChatOpenAI(model="gpt-5.4", api_key=OPENAI_API_KEY, temperature=temperature)
    elif PROVIDER == Provider.anthropic:
        llm = ChatAnthropic(model="claude-sonnet-4-6", api_key=ANTROPIC_API_KEY, temperature=temperature)

    if inputData is None:
        return "[WARNING] function 'callAi` no contained input"

    return llm.invoke([SystemMessage(SYSTEM_MESSAGE), HumanMessage(inputData)]).content

SYSTEM_MESSAGE = """
hi there you is helpfull asistant
"""


if __name__ == "__main__":
    print(callAi("hello"))
