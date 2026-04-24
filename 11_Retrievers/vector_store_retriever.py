from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="GoogleGenerativeAI provides powerful embedding models."),
]

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="ash297"
)

retriever = vectorstore.as_retriever(search_kwargs={'k' : 2})

query = "What is chroma?"

results = retriever.invoke(query)

for i , doc in enumerate(results):
    print(f"\n---- Result {i + 1} ----")
    print(doc.page_content)

# results = vectorstore.similarity_search(query, k=2)

# for i, doc in enumerate(results):
#     print(f"\n--- Result {i+1} ---")
#     print(doc.page_content)