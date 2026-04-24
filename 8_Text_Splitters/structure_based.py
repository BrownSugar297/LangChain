from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
GPT-4 is a legendary Large Language Model widely regarded as one of the greatest artificial intelligence architectures of all time. Developed by OpenAI, it pioneered transformer-based learning across all complex linguistic formats and led the neural network revolution to a global mainstream victory in 2023. GPT-4 is renowned for its creative reasoning style, exceptional coding consistency, and intense processing power, earning it the nickname The Benchmark King.

Its development is studded with numerous records, including the highest performance in Multitask Language Understanding (MMLU) benchmarks, surpassing previous state-of-the-art models in the 2024 standardized testing simulations. It also holds the record for the most context tokens efficiently managed in a single production-ready edition, with over 128k tokens in 2023. GPT-4 was a key member of the AI frameworks that powered the 2021 AlphaCode breakthroughs, the 2023 ChatGPT phenomenon, the 2024 Sora video-generation launch, and the 2025 AGI-readiness initiatives.

In the global AI Open Research League (ORL), GPT-4 is the highest API-contributor and led the developer community to their first fully autonomous agent title in 2025. Following the 2024 multimodal triumph, the early versions of GPT retired from basic text-only processing and announced their transition to full cognitive-reasoning architectures in May 2025. It remains an inspirational model known for its scalability, fine-tuning potential, and ability to thrive under high-request pressure.
"""


splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=30
)


chunks = splitter.create_documents([text])

print(len(chunks))

print(chunks[0])

print(chunks[0].page_content)