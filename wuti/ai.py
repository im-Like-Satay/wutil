import os
from dotenv import load_dotenv
from enum import Enum

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


class Provider(Enum):
    groq = 'groq'
    gemini = 'gemini'

def callAi(provider: Provider, inputData: str | None = None, temperature: float = 0.1):
    if provider == Provider.groq:
        llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", api_key=GROQ_API_KEY, temperature=temperature)
    elif provider == Provider.gemini:
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", api_key=GEMINI_API_KEY, temperature=temperature)

    if inputData is None:
        return "[WARNING] function 'callAi` no contained input"

    return llm.invoke([SystemMessage(SYSTEM_MESSAGE), HumanMessage(inputData)]).content

SYSTEM_MESSAGE = """
hi there you is helpfull asistant
"""


if __name__ == "__main__":
    print(callAi(Provider.groq, inputData="hello"))
