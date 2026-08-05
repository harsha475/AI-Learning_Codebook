from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

chain = (
    RunnablePassthrough.assign(
        answer=lambda x: llm.invoke(x["question"]).content
    )
)

response = chain.invoke({
    "question": "What is LangChain?"
})

print(response)