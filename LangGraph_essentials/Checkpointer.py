from typing import Annotated, TypedDict
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    return {
        "messages": [
            AIMessage(content=f"You said: {state['messages'][-1].content}")
        ]
    }


builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

config = {
    "configurable": {
        "thread_id": "user_1"
    }
}

graph.invoke(
    {"messages": [HumanMessage(content="My name is Harsha")]},
    config=config,
)

result = graph.invoke(
    {"messages": [HumanMessage(content="What did I just tell you?")]},
    config=config,
)

for message in result["messages"]:
    print(type(message).__name__, ":", message.content)
