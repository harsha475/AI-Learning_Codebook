from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key="")
class State(TypedDict):
    messages: Annotated[list, add_messages]
    approval: str
def chatbot(state: State):
    response = model.invoke(state["messages"])
    return {"messages": [response]}

    
def interrupt_node(state: State):
    approval = interrupt(
        {"question": "do you want to give me answer or not? tell yes or no.",
         })
    return {"approval":approval}
    
#build a state graph
builder = StateGraph(State)
checkpointer = MemorySaver()
#adding nodes
builder.add_node("chatbot", chatbot)
builder.add_node("interrupt_node", interrupt_node)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", "interrupt_node")
builder.add_edge('interrupt_node', END)


result = builder.compile(checkpointer=checkpointer)



while True:
    data = input("ask a question:")
    if data.lower() in ["exit","quit"]:
        break
    config={"configurable": {"thread_id": "1"}
                }
    graph = result.invoke(
        {"messages": [HumanMessage(content=data)]}
        ,config=config
    )
    approval = input("Do you want to see the answer? (yes/no): ")

    # Resume graph with human decision
    graph = result.invoke(
        Command(resume=approval),
        config=config
    )
    if approval.lower()== "yes":
        print("ai:",graph["messages"][-1].content)
