import uuid

import streamlit as st

from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

from backend import graph


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Nexora",
    page_icon="🤖",
    layout="centered"
)


# ============================================================
# SESSION STATE
# ============================================================

if "thread_id" not in st.session_state:

    st.session_state.thread_id = str(
        uuid.uuid4()
    )


if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# CONFIG
# ============================================================

config = {
    "configurable": {
        "thread_id": st.session_state.thread_id
    }
}


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("⚙️ Settings")

    st.write("### Features")

    st.success("✓ LangGraph")
    st.success("✓ Gemini 2.5 Flash")
    st.success("✓ Streaming")
    st.success("✓ SQLite Persistence")
    st.success("✓ Tavily Search")
    st.success("✓ Calculator Tool")
    st.success("✓ ToolNode")
    st.success("✓ Conditional Routing")

    st.divider()

    st.write("### Thread ID")

    st.code(
        st.session_state.thread_id
    )

    if st.button("🆕 New Chat"):

        st.session_state.thread_id = str(
            uuid.uuid4()
        )

        st.session_state.messages = []

        st.rerun()


# ============================================================
# TITLE
# ============================================================


st.title("🤖 Nexora AI")
st.caption("Intelligent AI Assistant powered by LangGraph")


# ============================================================
# LOAD SAVED CHAT
# ============================================================

if not st.session_state.messages:

    saved_state = graph.get_state(config)

    if saved_state.values:

        saved_messages = saved_state.values.get(
            "messages",
            []
        )

        for message in saved_messages:

            if isinstance(message, HumanMessage):

                st.session_state.messages.append(
                    {
                        "role": "user",
                        "content": message.content
                    }
                )

            elif isinstance(message, AIMessage):

                if message.content:

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": message.content
                        }
                    )


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Ask me anything..."
)


# ============================================================
# PROCESS MESSAGE
# ============================================================

if user_input:

    # --------------------------------------------------------
    # USER MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)


    # --------------------------------------------------------
    # ASSISTANT MESSAGE
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        full_response = ""


        # ----------------------------------------------------
        # STREAM LANGGRAPH
        # ----------------------------------------------------

        for message_token, metadata in graph.stream(

            {
                "messages": [
                    HumanMessage(
                        content=user_input
                    )
                ]
            },

            config=config,

            stream_mode="messages"
        ):

            # Only show chatbot output.
            # Tool output is hidden from the UI.

            if metadata.get(
                "langgraph_node"
            ) != "chatbot":

                continue


            content = message_token.content


            # ------------------------------------------------
            # NORMAL TEXT
            # ------------------------------------------------

            if isinstance(content, str):

                full_response += content


            # ------------------------------------------------
            # LIST CONTENT
            # ------------------------------------------------

            elif isinstance(content, list):

                for item in content:

                    if isinstance(item, dict):

                        text = item.get("text")

                        if text:

                            full_response += text


            # ------------------------------------------------
            # UPDATE STREAMLIT UI
            # ------------------------------------------------

            response_placeholder.markdown(
                full_response
            )


    # ========================================================
    # SAVE MESSAGE TO SESSION
    # ========================================================

    if full_response:

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": full_response
            }
        )