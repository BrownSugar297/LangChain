from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Ashikur Rahman Ashik"

result = embedding_model.embed_query(text)

print(str(result))

# For documents
documents = [
    "Paris is known for its iconic Eiffel Tower and rich cultural heritage.",
    "Large Language Models (LLMs) like Gemini use deep learning to understand human text.",
    "Bangladesh is a beautiful South Asian country known for the world's largest mangrove forest, the Sundarbans."
]

vector = embedding_model.embed_documents(documents)

print(str(vector))