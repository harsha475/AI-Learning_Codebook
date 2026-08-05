from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")
while True:
    question = input("Ask: ")
    if question.lower() in ["exit", "quit"]:
        print("bye")
        break
    response = llm.invoke(question)
    print(response.content)
