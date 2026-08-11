from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict

model = ChatOpenAI()
# create a state class
class State(TypedDict):
    user: str
    answer: str

def single_response(state: State):
    response = model.invoke(state["user"])
    return {"answer": response.content}
    
#build a state graph
builder = StateGraph(State)
#adding nodes

builder.add_node("single_response", single_response)
builder.add_edge(START, "single_response")
builder.add_edge("single_response", END)

result = builder.compile()
data = input("ask a question:")
final_answer = result.invoke(data)
print(final_answer)

