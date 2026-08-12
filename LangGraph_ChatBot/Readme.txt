# 🤖 Nexora AI — LangGraph Chatbot

An intelligent AI chatbot built with **LangGraph, Gemini 2.5 Flash, Tavily, SQLite, and Streamlit**.

This project demonstrates a stateful AI workflow with **tool calling, conditional routing, streaming, and persistent conversation history**.

## 🚀 Features

* 🧠 Gemini 2.5 Flash
* 🔗 LangGraph StateGraph
* 🛠️ Tool Calling
* 🌐 Tavily Web Search
* 🧮 Custom Calculator Tool
* 🔀 Conditional Routing
* ⚙️ LangGraph ToolNode
* ⚡ Streaming Responses
* 💾 SQLite Checkpointing
* 🧵 Thread-based Conversations
* 🎨 Streamlit UI

## 🏗️ Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
LangGraph
 │
 ▼
Gemini 2.5 Flash
 │
 ├── Normal Response ──► END
 │
 └── Tool Call
        │
        ▼
     ToolNode
      /     \
     ▼       ▼
 Tavily   Calculator
     \       /
      ▼     ▼
       Chatbot
          │
          ▼
         END

SQLite → Persistent Conversation State
```

## 🛠️ Technologies

* **Python**
* **LangGraph**
* **LangChain**
* **Gemini 2.5 Flash**
* **Tavily**
* **SQLite**
* **Streamlit**

## 📁 Project Structure

```text
langgraph-ai-chatbot/
│
├── backend.py
├── Ui.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🔧 Setup

Clone the repository:

```bash
git clone https://github.com/your-username/langgraph-ai-chatbot.git
cd langgraph-ai-chatbot
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Run the application:

```bash
python -m streamlit run Ui.py
```

## 💡 Example

```text
User: What are the latest developments in AI agents?

→ Gemini decides a web search is required
→ Tavily searches the web
→ ToolNode executes the tool
→ Result returns to Gemini
→ Response is streamed to the user
→ Conversation state is saved in SQLite
```

## 🎯 Key LangGraph Concepts

This project demonstrates:

**State → Nodes → Edges → Conditional Routing → Tool Calling → ToolNode → Streaming → Checkpointing → SQLite Persistence → Streamlit UI**

## 🚀 Future Improvements

* RAG with vector databases
* Multi-agent workflows
* Human-in-the-loop
* PostgreSQL persistence
* Authentication
* Cloud deployment

## 👨‍💻 Author

**Dalavai Harsha Sri Sumanth**

Computer Science graduate
AI/ML & Generative AI and Agentic Enthusiast

