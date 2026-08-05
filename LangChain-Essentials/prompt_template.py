from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple words."
)

chain = prompt | llm

response = chain.invoke({"topic": "LangChain"})

print(response.content)