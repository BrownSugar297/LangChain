from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'), 
    ('human', '{query}')
])

formatted_history = []
try:
    with open('chat_history.txt', 'r') as f:
        for line in f:
            line = line.strip() 
            if not line: continue 
            
            
            if line.startswith("Human:"):
                content = line.replace("Human:", "").strip()
                formatted_history.append(HumanMessage(content=content))
            
            
            elif line.startswith("AI:"):
                content = line.replace("AI:", "").strip()
                formatted_history.append(AIMessage(content=content))
except FileNotFoundError:
    print("Error: chat_history.txt file not found.")


prompt = chat_template.invoke({
    'chat_history': formatted_history, 
    "query": "where is my refund"
})

for msg in prompt.to_messages():
    print(msg)