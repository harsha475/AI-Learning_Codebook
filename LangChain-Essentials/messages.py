from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

messages = [
    SystemMessage(content="You are a Python teacher."),
    HumanMessage(content="Explain lists.")
]

response = llm.invoke(messages)

print(response.content)