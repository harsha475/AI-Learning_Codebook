from typing import Annotated, TypedDict

from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


# State
class State(TypedDict):
    messages: Annotated[list, add_messages]


# Chatbot node
def chatbot(state: State):

    # Get the existing messages
    messages = state["messages"]

    # Add AI message to the list
    messages.append(
        AIMessage(content="Hello! I received your message.")
    )

    # Return updated messages
    return {
        "messages": messages
    }


# Create graph
builder = StateGraph(State)

builder.add_node("chatbot", chatbot)

builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)


# Compile graph
graph = builder.compile()


# Give input
result = graph.invoke({
    "messages": [
        HumanMessage(content="Hi")
    ]
})


# Print messages
for message in result["messages"]:
    print(type(message).__name__, ":", message.content)
