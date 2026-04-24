from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

documents = [
    "Lionel Messi is an Argentine professional footballer who plays as a forward. Often considered the greatest player of all time, he has won a record eight Ballon d'Or awards and led Argentina to the 2022 FIFA World Cup title.",
    "Cristiano Ronaldo is a Portuguese professional footballer who plays as a forward. He is known for his goal-scoring ability, athleticism, and consistency. He has won five Ballon d'Or awards and is the top scorer in international football history.",
    "Kylian Mbappe is a French professional footballer who plays as a forward. He is known for his incredible speed, dribbling, and finishing skills. He won the 2018 FIFA World Cup and is considered one of the best young players in the world.",
    "Erling Haaland is a Norwegian professional footballer who plays as a striker. He is known for his goal-scoring, speed, and physicality. He plays for Manchester City and is widely regarded as one of the best finishers in modern football.",
    "Neymar Jr is a Brazilian professional footballer who plays as a forward. Known for his flair, dribbling skills, and playmaking ability, he is the all-time top goalscorer for the Brazil national team."
]

query = "Who is known for his incredible speed and finishing skills?"


documents_embeddings = embedding_model.embed_documents(documents)

query_embeddings = embedding_model.embed_query(query)

# Compute cosine similarity between the query embedding and all document embeddings
scores = cosine_similarity([query_embeddings], documents_embeddings)[0]

# Get the index and similarity score of the most relevant document
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is: ",score)

