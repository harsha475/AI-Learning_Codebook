# LangGraph Learning & Projects 🚀

This repository contains my learning journey with **LangGraph**, including practical examples of its core concepts and a chatbot project built using LangGraph.

## 📚 What I Learned

The repository covers important LangGraph concepts such as:

* State
* Nodes
* Edges
* START and END
* `add_messages`
* Reducers
* Conditional Edges
* Tool Calling
* ToolNode
* `tools_condition`
* Streaming
* Checkpointers
* MemorySaver
* SQLite Checkpointer
* Human-in-the-Loop
* Persistence
* Thread ID
* Chat History
* LangGraph workflows

## 🤖 LangGraph Chatbot

I also built a chatbot using LangGraph with features such as:

* 💬 Conversational chat
* ⚡ Streaming responses
* 🧠 Conversation memory
* 💾 Checkpointing
* 🗃️ SQLite persistence
* 👤 Human-in-the-Loop
* 🔄 Resume conversations using `thread_id`

The chatbot demonstrates how LangGraph can be used to build more structured and stateful LLM applications.

## 🛠️ Technologies Used

* Python
* LangGraph
* LangChain
* Google Gemini
* SQLite
* Python Typing
* LLMs

## 📂 Repository Structure

```text
LangGraph/
│
├── State/
├── Nodes/
├── Edges/
├── Reducers/
├── Conditional_Edges/
├── Tool_Calling/
├── ToolNode/
├── Streaming/
├── Checkpointer/
├── Human_in_the_Loop/
│
└── LangGraph_Chatbot/
    ├── Streaming
    ├── Persistence
    ├── Checkpointer
    ├── SQLite
    └── Human_in_the_Loop
```

## 🎯 Purpose

The main purpose of this repository is to understand **LangGraph concepts through practical coding examples** rather than only learning the theory.

Each example focuses on a specific concept and shows how it can be implemented in a real application.

## 🚀 Getting Started

Clone the repository:

```bash
git clone <your-repository-url>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Set your API key as an environment variable:

```bash
GOOGLE_API_KEY="your-api-key"
```

Then run any example:

```bash
python filename.py
```

## 📌 Key Takeaway

Through this repository, I explored how **LangGraph enables stateful, controllable, and production-oriented LLM workflows**, especially for applications involving memory, tools, streaming, persistence, and human interaction.

More examples and improvements will be added as I continue learning and building with LangGraph.

---

⭐ If you find this repository useful, feel free to explore the examples and give it a star!
