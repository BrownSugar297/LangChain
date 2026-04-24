from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

search_tool = DuckDuckGoSearchRun()

llm = ChatGroq(
    api_key=groq_api_key,
    model_name=("llama-3.1-8b-instant")
)

# Create the ReAct agent using LangGraph (modern approach)
agent = create_react_agent(
    model=llm,
    tools=[search_tool],
)

response = agent.invoke({
    "messages": [{"role": "user", "content": "3 ways to reach paris from london?"}]
})

print(response["messages"][-1].content)