from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    number: int
    result: str

def start_node(state: State):
    return {}


def route(state: State):
    if state["number"] % 2 == 0:
        return "even"
    return "odd"


def even_node(state: State):
    return {"result": "Even number"}


def odd_node(state: State):
    return {"result": "Odd number"}


builder = StateGraph(State)

builder.add_node("start", start_node)
builder.add_node("even", even_node)
builder.add_node("odd", odd_node)

builder.add_edge(START, "start")

builder.add_conditional_edges(
    "start",
    route,
    {
        "even": "even",
        "odd": "odd",
    },
)

builder.add_edge("even", END)
builder.add_edge("odd", END)

graph = builder.compile()

print(graph.invoke({"number": 7, "result": ""}))
