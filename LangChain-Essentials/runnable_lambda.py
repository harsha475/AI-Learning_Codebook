from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

# Custom Python function
def uppercase(text):
    return text.upper()

chain = RunnableLambda(uppercase) | llm

response = chain.invoke("what is langchain?")

print(response.content)