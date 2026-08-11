from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key="")
class State(TypedDict):
    messages: Annotated[list, add_messages]
    approval: str
def chatbot(state: State):
    response = model.invoke(state["messages"])
    return {"messages": [response]}




    
#build a state graph
builder = StateGraph(State)
checkpointer = MemorySaver()
#adding nodes
builder.add_node("chatbot", chatbot)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)


result = builder.compile(checkpointer=checkpointer)



while True:
    data = input("ask a question:")
    if data.lower() in ["exit","quit"]:
        break
    
    for message_token, metadata in result.stream(
        {"messages":[HumanMessage(content=data)]},
        config={"configurable": {"thread_id": "1"}},
        stream_mode = "messages"
    ):
        if message_token.content:
            print(message_token.content, end=' ', flush=True)
    print()




