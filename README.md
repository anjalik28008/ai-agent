# AI Agent using LangChain and LangGraph

An autonomous AI agent that decides which tool to use based on your question.

## Tools Available
- **Calculator** — solves math expressions
- **Word Counter** — counts words in text
- **Text Reverser** — reverses any text

## How it works
The agent uses LangGraph's ReAct framework — it reasons about the question, picks the right tool, uses it, and returns the answer autonomously.

## Tech Stack
- Python
- LangChain
- LangGraph
- Groq API (Llama 3)

## Setup
1. Clone the repo
2. Install: `pip install langchain langchain-groq langgraph ddgs python-dotenv`
3. Add Groq API key in `.env` file
4. Run: `python agent.py`
