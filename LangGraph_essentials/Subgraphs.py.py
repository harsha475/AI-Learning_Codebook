from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# -------------------------
# Child / Subgraph
# -------------------------

class ChildState(TypedDict):
    text: str


def child_node(state: ChildState):
    return {"text": state["text"] + " -> processed by subgraph"}


child_builder = StateGraph(ChildState)
child_builder.add_node("child_node", child_node)
child_builder.add_edge(START, "child_node")
child_builder.add_edge("child_node", END)

child_graph = child_builder.compile()


# -------------------------
# Parent Graph
# -------------------------

class ParentState(TypedDict):
    text: str


def parent_start(state: ParentState):
    return {"text": state["text"] + " -> parent"}


builder = StateGraph(ParentState)

builder.add_node("parent_start", parent_start)

# A compiled graph can be used as a node.
builder.add_node("subgraph", child_graph)

builder.add_edge(START, "parent_start")
builder.add_edge("parent_start", "subgraph")
builder.add_edge("subgraph", END)

graph = builder.compile()

result = graph.invoke({"text": "START"})

print(result)
