from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableBranch

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

coding_chain = llm
health_chain = llm
general_chain = llm

branch = RunnableBranch(
    (lambda x: "python" in x.lower(), coding_chain),
    (lambda x: "fever" in x.lower(), health_chain),
    general_chain
)

response = branch.invoke("Explain Python lists")

print(response.content)