LangChain
LangChain is a framework designed to simplify the development of applications powered by language models (like OpenAI's GPT, Anthropic's Claude, or open-source models like LLaMA and Mistral). It provides modular, composable components that connect LLMs, prompts, tools, memory, agents, retrievers, and more into structured, production-ready pipelines.
This repository documents a hands-on learning journey through LangChain's core components — from basic model invocation all the way through to building autonomous AI agents — with practical examples, mini-projects, and thorough explanations at every step.

📚 Table of Contents

Goals of This Repository
Current Progress

1. Chat Models
2. Prompts
3. Output Parsers
4. Structured Output
5. Chains
6. Runnable Primitives
7. Document Loaders
8. Text Splitters
9. Embedding Models
10. Vector Stores
11. Retrievers
12. RAG (Retrieval Augmented Generation)
13. Tool Calling
14. AI Agents
🎨 Bonus: AI Storyteller


Installation & Setup
Technologies Used
Contribution


🎯 Goals of This Repository

Learn and understand LangChain's main components through practical, hands-on coding examples.
Build small, functional mini-projects that demonstrate each component in a real context.
Document the journey in a structured, progressive way for educational and reference purposes.
Cover the full LangChain pipeline — from raw text input to autonomous agents — in a single cohesive repository.


🗂️ Current Progress

1️⃣ Chat Models
Folder: 1_Chat_Models/
This section focuses on LangChain's Model abstraction — the foundation of every LangChain pipeline. It covers how to invoke, configure, and compare both closed-source and open-source language models.
Models explored:

Closed-Source: OpenAI (gpt-4, gpt-4-turbo), Anthropic (claude-3), Google Gemini
Open-Source: Hugging Face models (TinyLlama, Mistral, Falcon) via langchain_huggingface

Topics covered:

Text generation and conversational invocation
Temperature, max_tokens, and sampling control
Synchronous invocation with .invoke() and streaming with .stream()
Comparing output quality and speed across providers

Example — Invoking a model:
pythonfrom langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.7)
response = llm.invoke([HumanMessage(content="Explain transformers in simple words.")])
print(response.content)

2️⃣ Prompts
Folder: 2_Prompts/
Learned how LangChain manages and structures prompts — the instructions given to language models. Prompts are the primary interface between the developer and the model, and LangChain provides powerful abstractions for making them reusable, dynamic, and composable.
Key concepts:

ChatPromptTemplate — Design reusable templates for conversations and structured inputs
MessagesPlaceholder — Insert dynamic message history or context into prompts
Message types: SystemMessage, HumanMessage, AIMessage

Topics covered:

Designing reusable and parameterized prompt templates
Managing conversation context using message placeholders
Combining system instructions with user input dynamically

Mini Projects:

Chatbot — Built a simple conversational chatbot using ChatPromptTemplate and message history
Research Paper Summarizer — Accepts a paper as input and produces a concise summary using a structured prompt template

Example — ChatPromptTemplate:
pythonfrom langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates to {language}."),
    ("human", "{text}")
])

formatted = prompt.format_messages(language="French", text="Hello, how are you?")

3️⃣ Output Parsers
Folder: 3_Output_Parsers/
Learned about Output Parsers — components that transform raw LLM text responses into structured, programmatically usable formats. Parsers are essential for building reliable, machine-readable pipelines.
Types of Output Parsers explored:
ParserDescriptionStrOutputParserReturns plain text output — ideal for simple, pass-through responsesJsonOutputParserParses model output formatted as JSON into Python dictionariesStructuredOutputParserEnforces a predefined schema using LangChain format instructionsPydanticOutputParserLeverages Pydantic models to parse and validate structured LLM responses
Topics covered:

Attaching parsers to chains using the pipe (|) operator
Injecting format instructions into prompt templates
Handling and recovering from parser errors gracefully

Example — JSON parsing in a chain:
pythonfrom langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

parser = JsonOutputParser()
prompt = ChatPromptTemplate.from_template(
    "Return a JSON object with 'name' and 'age' for a fictional person.\n{format_instructions}"
).partial(format_instructions=parser.get_format_instructions())

chain = prompt | ChatOpenAI() | parser
print(chain.invoke({}))

4️⃣ Structured Output
Folder: 4_Structured_Output/
Explored methods for getting structured, reliable, and validated outputs from LLMs — critical for building production-grade applications where responses must integrate with downstream code.
Methods learned:
TypedDict — Define expected output structure and guide the LLM's response shape:
pythonfrom typing import TypedDict

class MovieInfo(TypedDict):
    title: str
    genre: str
    rating: float
Pydantic — Enforce schema validation with automatic type checking:
pythonfrom pydantic import BaseModel, Field

class WeatherInfo(BaseModel):
    city: str
    temperature: float = Field(description="Temperature in Celsius")
    condition: str
.with_structured_output() — Bind a schema directly to the LLM for the cleanest integration:
pythonllm_with_schema = llm.with_structured_output(WeatherInfo)
result = llm_with_schema.invoke("What's the weather like in Tokyo?")
Topics covered:

When and why to use TypedDict vs Pydantic
Combining structured output with prompt templates
Ensuring machine-readable, validated model responses


5️⃣ Chains
Folder: 5_Chains/
Chains are the core abstraction for composing prompts, models, parsers, and logic into multi-step, reusable pipelines. This module explores four distinct chain patterns that handle progressively more complex workflows.
Chain types explored:
1. Simple Chains — A basic Prompt → LLM → Parser pipeline:
pythonchain = prompt | llm | StrOutputParser()
response = chain.invoke({"product": "AI-powered drones"})
2. Sequential Chains — Output of one chain feeds as input to the next:
[Prompt 1 → LLM → Parser] → [Prompt 2 → LLM → Parser]
3. Parallel Chains — Multiple chains run simultaneously on the same input:
pythonchain = RunnableParallel(
    summary=summary_chain,
    sentiment=sentiment_chain
)
result = chain.invoke({"text": "LangChain is incredibly powerful!"})
# Returns: {"summary": "...", "sentiment": "..."}
4. Conditional Chains — Route to different chains based on input content:
pythonbranch = RunnableBranch(
    (lambda x: "weather" in x["query"].lower(), weather_chain),
    general_chain  # default fallback
)
Topics covered:

Composing multi-step pipelines using the pipe (|) operator
Sequential, parallel, and conditional execution patterns
Controlling and transforming data flow between components


6️⃣ Runnable Primitives
Folder: 6_Runnable_Primitives/
A deep dive into LangChain's Runnable interface — the execution engine that powers every pipeline. Runnables are composable units that take an input, process it, and return an output. Every LangChain component (models, prompts, parsers, retrievers, tools) is a Runnable.
Why Runnables? They replace rigid older chain classes with high modularity, flexible composition, parallel and conditional execution, custom Python logic insertion, and a unified interface across all LangChain components.
Every Runnable supports:

.invoke(input) — synchronous execution
.ainvoke(input) — async execution
.batch(inputs) — multiple inputs processed in parallel
.stream(input) — token-by-token output streaming
| (pipe operator) — Unix-style component composition

Primitives explored:
PrimitivePurposeRunnableSequenceExecute steps one after another; output of A becomes input to BRunnableParallelRun multiple branches simultaneously on the same inputRunnableLambdaWrap any Python function as a composable RunnableRunnablePassthroughPass input unchanged — useful for fan-out and merge patternsRunnableBranchConditional routing — equivalent to if / elif / else
Key learnings:

Runnables are the most powerful and flexible abstraction in LangChain
RunnableLambda enables inserting custom Python logic anywhere in a pipeline
RunnableParallel is essential for generating multiple perspectives from a single input
All LangChain modules — models, retrievers, tools, prompts — are plug-and-play Runnables


7️⃣ Document Loaders
Folder: 7_Document_Loaders/
Document Loaders are the entry point of any retrieval or RAG pipeline. They provide a unified interface for ingesting data from diverse sources — files, web pages, APIs, and entire directories — into a consistent Document format that LangChain understands.
Loaders covered:
LoaderSourceTextLoaderPlain .txt filesPyPDFLoaderMulti-page PDF documentsCSVLoaderCSV files, loaded row-by-row as DocumentsWebBaseLoaderHTML content from any URLDirectoryLoaderAll files in a folder with automatic loader selection
How Document Loaders work — Every loader outputs a uniform Document structure:
python{
  "page_content": "...actual text...",
  "metadata": {
      "source": "filename.pdf",
      "page": 1
  }
}
This uniform structure seamlessly feeds into chunking, embedding, vector storage, and retrieval — regardless of the original file format.

8️⃣ Text Splitters
Folder: 8_Text_Splitters/
Text Splitters divide large documents into smaller, manageable chunks optimized for embedding and retrieval. Chunking strategy directly affects the quality of semantic search and RAG outputs.
Why split text?

LLMs and embedding models have hard context window limits
Smaller, focused chunks produce more precise retrieval results
Proper chunking ensures semantic coherence within each chunk

Splitter types explored:
1. Length-Based (CharacterTextSplitter) — Splits by character count; ideal for uniform chunking of plain text.
2. Structure-Based (RecursiveCharacterTextSplitter) — Splits recursively on natural separators (paragraphs → sentences → words). The recommended default for most use cases.
3. Language-Aware (RecursiveCharacterTextSplitter.from_language) — Respects code and document structure: Python class/function boundaries, Markdown headers, and more.
4. Semantic (SemanticChunker) — Uses embedding similarity to detect topic shifts and split on meaning rather than characters. Produces the most contextually coherent chunks:
pythonfrom langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation"
)
docs = splitter.create_documents([long_text])

9️⃣ Embedding Models
Folder: 9_Embedding_Models/
Explored how embedding models convert text into high-dimensional numerical vectors that capture semantic meaning. Embeddings are the foundation of every semantic search, retrieval, and RAG system.
Models covered:

Closed-Source: OpenAI (text-embedding-3-small, text-embedding-3-large)
Open-Source: Hugging Face sentence-transformers models

Topics covered:

Generating embeddings for documents and queries
Computing cosine similarity between vectors using scikit-learn
Understanding why semantically similar text produces nearby vectors in embedding space

Mini Project — Semantic Search:
1. Embed a collection of text documents
2. Embed a user query
3. Compute cosine similarity between query and all documents
4. Return the top-matching document and its similarity score
This project demonstrates the core retrieval principle powering all modern semantic search systems.

🔟 Vector Stores
Folder: 10_Vector_Stores/
A Vector Store is a specialized storage system for managing and querying high-dimensional vector embeddings at scale. It is the backbone of any semantic search or RAG system, enabling fast approximate nearest neighbor (ANN) lookup across large document collections.
Vector Store vs. Vector Database:
AspectVector StoreVector DatabaseFocusEmbedding storage and similarity searchBroader data management + vector searchFeaturesIndex, search, retrieveTransactions, governance, metadata queriesScaleSmall to medium deploymentsEnterprise-scale, billions of vectors
Stores integrated in this module:
StoreTypeBest ForFAISSOpen-source, localFast local deployments, lightweight appsChromaDBOpen-source, in-memory/diskQuick setup, development and prototypingPineconeManaged cloudAuto-scaling, production workloadsWeaviateOpen-sourceHybrid search + knowledge graphsQdrantOpen-sourceAdvanced metadata filtering + personalized search
Key features covered:

Indexing documents with embeddings using .add_documents()
Performing similarity search with .similarity_search(query, k=5)
Filtering results by metadata
Persisting and reloading vector stores to/from disk


1️⃣1️⃣ Retrievers
Folder: 11_Retrievers/
Retrievers provide a unified interface for fetching relevant documents from any data source based on a natural language query. They abstract over vector stores, APIs, and search engines, returning a standardized list of Document objects ready for downstream processing.
Retriever types explored:
1. Vector Store Retriever — The most common retriever; performs similarity search over FAISS/Chroma/Pinecone.
2. Wikipedia Retriever — Queries the Wikipedia API directly for general-knowledge retrieval.
3. MMR (Maximum Marginal Relevance) Retriever — Balances relevance and diversity to eliminate redundant results:
pythonretriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 5})
4. Multi-Query Retriever — Automatically generates multiple rephrasings of a query, runs them all, and merges the results — dramatically improving recall for ambiguous queries.
5. Contextual Compression Retriever — Wraps another retriever and compresses/filters retrieved chunks to only the most relevant portions, reducing noise in the LLM's context window.
Retriever output format:
python{
  "page_content": "...relevant document content...",
  "metadata": {
      "source": "source_name",
      "score": 0.95
  }
}

1️⃣2️⃣ Retrieval Augmented Generation (RAG)
Folder: 12_Rag/
RAG is an architecture that combines an LLM with an external knowledge source, enabling the model to generate answers grounded in real, custom, and up-to-date information — rather than relying solely on its training data.
RAG = Retriever + LLM
Why RAG?

Overcomes the LLM knowledge cutoff with live, domain-specific data
Reduces hallucinations by constraining answers to retrieved context
Enables use of private and proprietary documents without fine-tuning
The knowledge base can be updated anytime — the LLM uses it immediately

Full RAG Pipeline implemented:
[1. Load Documents]
        ↓
[2. Split into Chunks]
        ↓
[3. Generate Embeddings]
        ↓
[4. Store in Vector Store (FAISS / ChromaDB)]
        ↓
[5. Embed User Query at Runtime]
        ↓
[6. Retrieve Top-k Similar Chunks]
        ↓
[7. Inject Context into Prompt Template]
        ↓
[8. LLM Generates Grounded Answer]
RAG Prompt Template:
pythonprompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Answer only from the provided context.
If the context is insufficient, say "I don't know."

Context:
{context}

Question:
{question}
""")
Topics covered:

End-to-end RAG pipeline construction
Using create_retrieval_chain and create_stuff_documents_chain
Combining FAISS retrieval with OpenAI generation
Evaluating answer grounding and retrieval quality


1️⃣3️⃣ Tool Calling
Folder: 13_Tool_Calling/
Tool Calling is the mechanism by which an LLM decides to invoke an external function, generates the correct structured arguments, and returns a tool call object instead of a plain text response. LangChain provides a unified interface for tool calling across OpenAI, Anthropic, Groq, and Google models.
Three tool creation methods explored:
1. @tool Decorator — Simplest approach; automatically infers schema from type hints:
pythonfrom langchain_core.tools import tool

@tool
def get_stock_price(ticker: str) -> float:
    """Returns the current stock price for a given ticker symbol."""
    return fetch_price(ticker)
2. StructuredTool — Uses Pydantic for strict input validation; recommended for production:
pythonfrom langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class SearchInput(BaseModel):
    query: str = Field(description="The search query string")

search_tool = StructuredTool.from_function(
    func=search_web,
    name="web_search",
    description="Search the web for current information",
    args_schema=SearchInput
)
3. BaseTool — Full control over custom logic, async behavior, and initialization.
The Tool Calling Pipeline:
StepWhat HappensCodeBindAttach tools to the LLMllm.bind_tools([tool1, tool2])CallLLM decides to invoke a toolModel outputs a structured tool_call objectExecuteLangChain runs the functionArguments validated → function executes → result returned
Toolkits covered: SQL Toolkit, File Toolkit, VectorStore Toolkit — pre-built collections of domain-specific tools for rapid agent development.

1️⃣4️⃣ AI Agents
Folder: 14_AI_Agents/
AI Agents use an LLM as a reasoning engine to autonomously decide which actions to take, execute those actions using tools, observe the results, and iterate until the task is complete. This module implements the ReAct (Reasoning + Acting) agent pattern.
What is a ReAct Agent?
ReAct agents alternate between two phases in a tight loop:
[Observe Input]
      ↓
[Reason: What should I do next?]
      ↓
[Act: Call a tool OR return final answer]
      ↓
[Observe tool result]
      ↓
[Reason again...] ← repeat until task is complete
Implementation:
pythonfrom langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Pull standard ReAct prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

response = agent_executor.invoke({"input": "What is the current weather in Tokyo?"})
Tools integrated:

DuckDuckGo Search — Real-time web search for up-to-date information
Calculator — Reliable arithmetic to prevent LLM math errors
Custom domain tools — Built with the @tool decorator

Topics covered:

Building ReAct agents from scratch and with create_react_agent
AgentExecutor configuration: verbose, max_iterations, handle_parsing_errors
Observing the full chain-of-thought reasoning trace in verbose mode
Adding persistent memory for multi-turn agent conversations
