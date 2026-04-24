from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")


text_splitter = SemanticChunker(
    embeddings, 
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. 

My name is Ashikur Rahman. I am interested in learning about AI and its applications. I have been exploring various AI models and their capabilities, and I am excited to see how they can be used to solve real-world problems.

Silicon Valley is the biggest technology hub in the world. People all over the world use the software and hardware developed here and support their favorite tech giants.

Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""


docs = text_splitter.create_documents([sample])

print(f"Total Semantic Chunks: {len(docs)}")

for i, doc in enumerate(docs):
    print(f"\n--- Chunk {i+1} ---")
    print(doc.page_content)