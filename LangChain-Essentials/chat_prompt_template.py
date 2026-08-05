from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])

history = [
    HumanMessage(content="My name is Harsha."),
    AIMessage(content="Nice to meet you, Harsha!")
]

chain = prompt | llm

response = chain.invoke({
    "history": history,
    "question": "What is my name?"
})

print(response.content)