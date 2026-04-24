from loader import get_youtube_transcript
from splitter import split_transcript_into_chunks
from vector_store import store_chunks_in_vectorstore
from retrieval import retrieve_relevant_documents
from augmentation import create_context_prompt
from generation import run_llm

# 1. Load
transcript = get_youtube_transcript()

# 2. Split
chunks = split_transcript_into_chunks(transcript)

# 3. Store
vs_result = store_chunks_in_vectorstore(chunks)
vector_store = vs_result["vector_store"]

# 4. Retrieve
query = "What is the Golden Circle and what does WHY mean?"
docs = retrieve_relevant_documents(query, vector_store)

# 5. Augment
context = "\n\n".join([doc.page_content for doc in docs])
prompt_template = create_context_prompt()
prompt = prompt_template.format(context=context, query=query)

# 6. Generate
answer = run_llm(prompt)
print("Answer:", answer)