from langchain_groq import ChatGroq
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

# Tool Creation
@tool
def multiply(a : int, b : int) -> int:
    """Multiply two numbers"""
    return a * b

# LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Tool Binding
llm_with_tools = llm.bind_tools([multiply])

# llm_with_tools.invoke("Hello")

result = llm_with_tools.invoke("Can you multiply 2 by 5?").tool_calls[0]


print(result)

# LLM does not actually run the tool - It just suggests the tool and the input arguments.
# The actual execution is handled by LangChain or programmer.