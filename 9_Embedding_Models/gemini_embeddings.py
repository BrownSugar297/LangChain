from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from dotenv import load_dotenv  

load_dotenv()  


embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview") 


result = embeddings.embed_query("Lucknow is the capital of UttarPradesh")  

print(str(result))  


documents = [
    "Paris is known for its iconic Eiffel Tower and rich cultural heritage.",
    "Large Language Models (LLMs) like Gemini use deep learning to understand human text.",
    "Bangladesh is a beautiful South Asian country known for the world's largest mangrove forest, the Sundarbans."
]

result = embeddings.embed_documents(documents, output_dimensionality=768)

print(f"Number of Document Embeddings: {len(result)}")
print(f"Sample Embedding from first document: {result[0][:5]}...")
print(str(result))
