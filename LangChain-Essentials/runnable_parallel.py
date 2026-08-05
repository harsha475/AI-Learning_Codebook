from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

parallel = RunnableParallel(
    summary=llm,
    translate=llm,
    sentiment=llm
)

response = parallel.invoke("LangChain is amazing!")

print(response)
