# ChatGroq class for chat-based LLMs from LangChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Initialize the chat-based LLM
chat_model = ChatGroq(model="llama-3.3-70b-versatile")

# Send a user message to the model and get its response
response = chat_model.invoke("Who is the prime minister of moon?")

print(response.content)


# Streaming response
chat_model = ChatGroq(model="llama-3.3-70b-versatile", streaming=True)

def stream_response(prompt):
    response = chat_model.stream(prompt)

    for chunk in response:
        print(chunk.content, end="")

stream_response("Write 10 lines on langchain")
