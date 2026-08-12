import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

from typing import TypedDict, Annotated

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_tavily import TavilySearch

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite import SqliteSaver


# ============================================================
# API KEYS
# ============================================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is not set")


# ============================================================
# MODEL
# ============================================================

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)


# ============================================================
# STATE
# ============================================================

class State(TypedDict):
    messages: Annotated[list, add_messages]


# ============================================================
# USER-DEFINED TOOL
# ============================================================

@tool
def calculator(expression: str) -> str:
    """
    Calculate mathematical expressions.

    Use this tool for addition, subtraction,
    multiplication and division.
    """

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"


# ============================================================
# TAVILY SEARCH TOOL
# ============================================================

tavily_search = TavilySearch(
    max_results=3,
    tavily_api_key=TAVILY_API_KEY
)


# ============================================================
# TOOLS
# ============================================================

tools = [
    tavily_search,
    calculator
]


# ============================================================
# MODEL WITH TOOLS
# ============================================================

model_with_tools = model.bind_tools(tools)


# ============================================================
# CHATBOT NODE
# ============================================================

def chatbot(state: State):

    response = model_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# ============================================================
# SQLITE CHECKPOINTER
# ============================================================

connection = sqlite3.connect(
    "storage.db",
    check_same_thread=False
)

checkpointer = SqliteSaver(connection)


# ============================================================
# BUILD GRAPH
# ============================================================

builder = StateGraph(State)


builder.add_node(
    "chatbot",
    chatbot
)

builder.add_node(
    "tools",
    ToolNode(tools)
)


# ============================================================
# GRAPH EDGES
# ============================================================

builder.add_edge(
    START,
    "chatbot"
)

builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

builder.add_edge(
    "tools",
    "chatbot"
)


# ============================================================
# COMPILE
# ============================================================

graph = builder.compile(
    checkpointer=checkpointer
)