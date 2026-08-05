from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableMap

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

mapper = RunnableMap({
    "summary": llm,
    "keywords": llm,
    "title": llm
})

response = mapper.invoke("LangChain is a framework for building LLM applications.")

print(response)