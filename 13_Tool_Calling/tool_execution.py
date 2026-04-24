from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage # ToolMessage ইমপোর্ট করা হয়েছে
from dotenv import load_dotenv

load_dotenv()


@tool
def multiply(a : int, b : int) -> int:
    """Multiply two numbers"""
    return a * b


llm = ChatGroq(model="llama-3.3-70b-versatile")

llm_with_tools = llm.bind_tools([multiply])


query = "Can you multiply 2 by 5?"
messages = [HumanMessage(content=query)]
ai_msg = llm_with_tools.invoke(messages) 
tool_call = ai_msg.tool_calls[0] 

tool_output = multiply.invoke(tool_call["args"]) 


tool_message = ToolMessage(
    content=str(tool_output), 
    tool_call_id=tool_call["id"]
)

print(f"Result: {tool_output}")