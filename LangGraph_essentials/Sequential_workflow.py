from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict

model = ChatOpenAI(api_key="sk-5678mnopqrstuvwx5678mnopqrstuvwx5678mnop", temperature=0.7)
# create a state class
class State(TypedDict):
    topic: str
    answer: str
def detailed_content(state:State):
    response = model.invoke(f"generate detailed answer for the topic,{state["topic"]}")
    return {"answer":response.content}
def summary_content(state:State):
    response = model.invoke(f"generate detailed summary for the topic,{state["answer"]}")
    return {"answer": response.content}
builder = StateGraph(State)
builder.add_node("detailed_content", detailed_content)
builder.add_node("summary_content", summary_content)
builder.add_edge(START, "detailed_content")
builder.add_edge("detailed_content", "summary_content")
builder.add_edge("summary_content", END)

result = builder.compile()
topic = input("enter the topic:")
final_answer = result.invoke({"topic": topic})
print(final_answer)
