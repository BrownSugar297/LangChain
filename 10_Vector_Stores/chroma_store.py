from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

from langchain_core.documents import Document

doc1 = Document(
    page_content="bKash is the largest MFS provider in Bangladesh. It revolutionized mobile payments and financial inclusion, offering services like money transfer, bill payments, and merchant payments through its robust fintech platform.",
    metadata={"industry": "FinTech", "headquarters": "Dhaka"}
)

doc2 = Document(
    page_content="Pathao is a leading Bangladeshi tech giant known for its ride-sharing, food delivery, and courier services. It has evolved into a 'Super App' ecosystem, significantly impacting the local gig economy.",
    metadata={"industry": "E-commerce & Logistics", "headquarters": "Dhaka"}
)

doc3 = Document(
    page_content="TigerIT is a major software company in Bangladesh specializing in biometrics and large-scale government projects. They are well-known for developing national ID systems and driver's license solutions globally.",
    metadata={"industry": "Software Development", "headquarters": "Dhaka"}
)

doc4 = Document(
    page_content="Brain Station 23 (BS23) is one of the largest software exporting companies in Bangladesh. They provide enterprise solutions, cloud computing, and AI services to global clients, including international banks and pharma giants.",
    metadata={"industry": "Software Export & IT Services", "headquarters": "Dhaka"}
)

doc5 = Document(
    page_content="Grameenphone (GP) has a massive digital wing focused on IoT, Cloud services, and enterprise IT solutions. As a telecom leader, they drive digital transformation for businesses across Bangladesh.",
    metadata={"industry": "Telecommunications & IT", "headquarters": "Bashundhara"}
)

docs = [doc1, doc2, doc3, doc4, doc5]

vectore_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview"),
    persist_directory='ashik_db',
    collection_name='ash297'
)

# after first run, you can comment out the add_documents line to avoid adding duplicates on subsequent runs
#vectore_store.add_documents(docs)

vectore_store.get(include=['embeddings','documents','metadatas'])


similarity_search = vectore_store.similarity_search(
    query="Which company is focused on software export and global clients?",
    k=2
)
print("--- Similarity Search Results ---")
for doc in similarity_search:
    print(f"Content: {doc.page_content}\nMetadata: {doc.metadata}\n")


similarity_search_with_score = vectore_store.similarity_search_with_score(
    query="Which is the largest mobile financial service or fintech provider?",
    k=1
)
print("--- Search with Score Results ---")
print(similarity_search_with_score)


filtered_results = vectore_store.similarity_search_with_score(
    query="Tell me about TigerIT", 
    filter={'industry': "Software Development"},
    k=1
)

print(filtered_results)