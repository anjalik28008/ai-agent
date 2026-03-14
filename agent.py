import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# Load API key
load_dotenv()

# Load LLM
llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

# Tool 1 - Calculator
@tool
def calculator(expression: str) -> str:
    """Useful for math calculations. Input must be a valid math expression like '25 * 48' or '100 / 4'."""
    try:
        result = eval(expression)
        return f"The answer is {result}"
    except:
        return "Could not calculate that."

# Tool 2 - Word Counter
@tool
def word_counter(text: str) -> str:
    """Counts the number of words in a given text."""
    count = len(text.split())
    return f"The text has {count} words."

# Tool 3 - Text Reverser
@tool
def text_reverser(text: str) -> str:
    """Reverses any given text or sentence."""
    return f"Reversed: {text[::-1]}"

# List of tools
tools = [calculator, word_counter, text_reverser]

# Create agent
agent = create_react_agent(llm, tools)

# Chat loop
print("\n✅ AI Agent ready!")
print("Tools available: Calculator, Word Counter, Text Reverser")
print("Example questions:")
print("  - What is 25 multiplied by 48?")
print("  - How many words are in 'hello world this is an AI agent'?")
print("  - Reverse the text 'LangChain is awesome'")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    try:
        result = agent.invoke({"messages": [("human", question)]})
        print(f"\nAgent: {result['messages'][-1].content}\n")
    except Exception as e:
        print(f"Error: {e}\n")