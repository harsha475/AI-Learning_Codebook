from typing import Annotated, TypedDict
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from dotenv import load_dotenv


load_dotenv()


@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


tools = [add]

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
).bind_tools(tools)


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    response = model.invoke(state["messages"])
    return {"messages": [response]}


builder = StateGraph(State)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "chatbot")

builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

builder.add_edge("tools", "chatbot")

graph = builder.compile()

result = graph.invoke({
    "messages": [
        HumanMessage(content="What is 20 + 30?")
    ]
})

print(result["messages"][-1].content)
