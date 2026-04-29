# LangChain

**LangChain** is a framework designed to simplify the development of applications powered by language models (like OpenAI's GPT, Anthropic's Claude, or open-source models like LLaMA and Mistral). It provides **modular, composable components** that connect LLMs, prompts, tools, memory, agents, retrievers, and more into structured, production-ready pipelines.

This repository documents a hands-on learning journey through LangChain's core components — from basic model invocation all the way through to building autonomous AI agents — with practical examples, mini-projects, and thorough explanations at every step.

---

## 📚 Table of Contents

- [Goals of This Repository](#-goals-of-this-repository)
- [Current Progress](#-current-progress)
  - [1. Chat Models](#1️⃣-chat-models)
  - [2. Prompts](#2️⃣-prompts)
  - [3. Output Parsers](#3️⃣-output-parsers)
  - [4. Structured Output](#4️⃣-structured-output)
  - [5. Chains](#5️⃣-chains)
  - [6. Runnable Primitives](#6️⃣-runnable-primitives)
  - [7. Document Loaders](#7️⃣-document-loaders)
  - [8. Text Splitters](#8️⃣-text-splitters)
  - [9. Embedding Models](#9️⃣-embedding-models)
  - [10. Vector Stores](#🔟-vector-stores)
  - [11. Retrievers](#1️⃣1️⃣-retrievers)
  - [12. RAG](#1️⃣2️⃣-rag-retrieval-augmented-generation)
  - [13. Tool Calling](#1️⃣3️⃣-tool-calling)
  - [14. AI Agents](#1️⃣4️⃣-ai-agents)
  - [🎨 Bonus: AI Storyteller](#-bonus-ai-storyteller)
- [Installation & Setup](#-installation--setup)
- [Technologies Used](#-technologies-used)
- [Contribution](#-contribution)

---

## 🎯 Goals of This Repository

- Learn and understand **LangChain's core components** through practical, hands-on coding examples.
- Build small, functional **mini-projects** that demonstrate each component in a real context.
- Document the journey in a **structured, progressive way** for educational and reference purposes.
- Cover the **full LangChain pipeline** — from raw text input to autonomous agents — in a single cohesive repository.

---

## 🗂️ Current Progress

---

### 1️⃣ Chat Models

**Folder:** `1_Chat_Models/`

The foundation of every LangChain pipeline. This section covers how to invoke, configure, and compare both closed-source and open-source language models through LangChain's unified model abstraction.

**Models explored:**
- **Closed-Source:** OpenAI (`gpt-4`, `gpt-4-turbo`), Anthropic (`claude-3`), Google Gemini
- **Open-Source:** Hugging Face models (TinyLlama, Mistral, Falcon) via `langchain_huggingface`

**Topics covered:**
- Text generation and conversational invocation
- Temperature, `max_tokens`, and sampling control
- Synchronous invocation with `.invoke()` and streaming with `.stream()`
- Comparing output quality and speed across providers

**Example — Invoking a model:**
```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.7)
response = llm.invoke([HumanMessage(content="Explain transformers in simple words.")])
print(response.content)
```

---

### 2️⃣ Prompts

**Folder:** `2_Prompts/`

Prompts are the primary interface between the developer and the model. This section covers how LangChain manages and structures prompts — making them reusable, dynamic, and composable.

**Key concepts:**
- `ChatPromptTemplate` — Design reusable templates for conversations and structured inputs
- `MessagesPlaceholder` — Insert dynamic message history or context into prompts
- Message types: `SystemMessage`, `HumanMessage`, `AIMessage`

**Topics covered:**
- Designing reusable and parameterized prompt templates
- Managing conversation context using message placeholders
- Combining system instructions with user input dynamically

**Mini Projects:**
- **Chatbot** — A simple conversational chatbot using `ChatPromptTemplate` and message history
- **Research Paper Summarizer** — Accepts a paper as input and produces a concise summary using a structured prompt template

**Example — ChatPromptTemplate:**
```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates to {language}."),
    ("human", "{text}")
])

formatted = prompt.format_messages(language="French", text="Hello, how are you?")
```

---

### 3️⃣ Output Parsers

**Folder:** `3_Output_Parsers/`

Output Parsers transform raw LLM text responses into structured, programmatically usable formats — essential for building reliable, machine-readable pipelines.

**Types of Output Parsers explored:**

| Parser | Description |
|---|---|
| `StrOutputParser` | Returns plain text output — ideal for simple, pass-through responses |
| `JsonOutputParser` | Parses model output formatted as JSON into Python dictionaries |
| `StructuredOutputParser` | Enforces a predefined schema using LangChain format instructions |
| `PydanticOutputParser` | Leverages Pydantic models to parse and validate structured LLM responses |

**Topics covered:**
- Attaching parsers to chains using LCEL (`|` operator)
- Enforcing schema constraints on model outputs
- Handling and recovering from malformed model responses

**Example — JSON Output Parser:**
```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

parser = JsonOutputParser()
prompt = PromptTemplate(
    template="Return a JSON object with name and age for a person named {name}.\n{format_instructions}",
    input_variables=["name"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
```

---

### 4️⃣ Structured Output

**Folder:** `4_Structured_Output/`

A deeper dive into forcing LLMs to return well-defined, validated data structures using Pydantic and TypedDict — the backbone of reliable agentic applications.

**Topics covered:**
- Defining structured schemas with Pydantic `BaseModel` and `TypedDict`
- Using `.with_structured_output()` to bind schemas directly to models
- Comparing Pydantic vs TypedDict for different use cases
- Validating and handling structured responses in pipelines

**Example — Pydantic structured output:**
```python
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

class MovieReview(BaseModel):
    title: str
    rating: float
    summary: str

llm = ChatOpenAI(model="gpt-4-turbo")
structured_llm = llm.with_structured_output(MovieReview)
result = structured_llm.invoke("Review the movie Inception.")
```

---

### 5️⃣ Chains

**Folder:** `5_Chains/`

Chains are the core compositional unit of LangChain — sequences of components linked together using the **LangChain Expression Language (LCEL)**. This module covers everything from simple single-step chains to complex parallel and conditional pipelines.

**Topics covered:**
- Building chains with the `|` (pipe) operator — LCEL syntax
- Sequential chains: passing output of one step as input to the next
- Parallel chains: running multiple branches simultaneously with `RunnableParallel`
- Conditional chains: routing to different branches based on input content
- Visualizing chain structure with `.get_graph().print_ascii()`

**Chain types:**

```
Simple:       [Prompt] → [Model] → [Parser]

Sequential:   [Chain A] → [Chain B] → [Chain C]

Parallel:     [Input] → [Branch A] ─┐
                      → [Branch B] ─┤ → [Merge]
                      → [Branch C] ─┘

Conditional:  [Input] → [Classifier] → (topic A) → [Chain A]
                                     → (topic B) → [Chain B]
```

**Example — Simple LCEL chain:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"]
)

chain = prompt | ChatGoogleGenerativeAI(model="gemini-2.5-flash") | StrOutputParser()
result = chain.invoke({"topic": "Black Holes"})
```

---

### 6️⃣ Runnable Primitives

**Folder:** `6_Runnable_Primitives/`

LangChain's Runnable primitives are the low-level building blocks that power LCEL. Understanding these unlocks fine-grained control over how data flows, branches, and transforms within any chain.

**Primitives covered:**

| Primitive | Purpose |
|---|---|
| `RunnableSequence` | Chains runnables sequentially — the backbone of `\|` syntax |
| `RunnableParallel` | Executes multiple runnables in parallel and merges outputs |
| `RunnablePassthrough` | Passes input through unchanged — useful for injecting context |
| `RunnableLambda` | Wraps any Python function as a runnable component |
| `RunnableBranch` | Conditionally routes to different runnables based on input |

**Topics covered:**
- Composing primitives manually vs. using LCEL sugar syntax
- Injecting passthrough data alongside transformed outputs
- Branching logic without external orchestrators
- Wrapping custom functions as chain-compatible components

---

### 7️⃣ Document Loaders

**Folder:** `7_Document_Loaders/`

Document Loaders are LangChain's interface for ingesting raw content from the real world — the first step in any RAG or knowledge pipeline. This module covers loading from a wide variety of source types.

**Loaders explored:**
- `TextLoader` — Plain `.txt` files
- `PyPDFLoader` / `PDFPlumberLoader` — PDF documents
- `CSVLoader` — Tabular CSV data
- `DirectoryLoader` — Recursively load all files from a directory
- `WebBaseLoader` — Scrape and load content from web URLs

**Topics covered:**
- Loading and inspecting `Document` objects (page content + metadata)
- Handling encoding issues and multi-page documents
- Loading entire directories with glob patterns
- Extracting structured content from web pages

**Example — Loading a PDF:**
```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("document.pdf")
pages = loader.load()
print(f"Loaded {len(pages)} pages")
print(pages[0].page_content[:200])
```

---

### 8️⃣ Text Splitters

**Folder:** `8_Text_Splitters/`

Before documents can be embedded and stored in vector databases, they must be split into manageable chunks. This module covers LangChain's splitting strategies — each suited to different content types and use cases.

**Splitters explored:**

| Splitter | Best For |
|---|---|
| `CharacterTextSplitter` | Simple length-based splitting |
| `RecursiveCharacterTextSplitter` | General-purpose; respects paragraph and sentence boundaries |
| `MarkdownHeaderTextSplitter` | Splits Markdown by header hierarchy |
| `HTMLHeaderTextSplitter` | Structure-aware splitting for HTML content |
| `SemanticChunker` | Groups sentences by semantic similarity using embeddings |

**Topics covered:**
- Choosing `chunk_size` and `chunk_overlap` effectively
- Preserving document structure during splitting
- Semantic chunking for meaning-aware splits
- Inspecting and validating chunk quality

---

### 9️⃣ Embedding Models

**Folder:** `9_Embedding_Models/`

Embeddings convert text into dense numerical vectors that capture semantic meaning — the core of all semantic search and RAG systems. This module covers both API-based and local embedding solutions.

**Models explored:**
- `GoogleGenerativeAIEmbeddings` — Gemini embedding API
- `SentenceTransformerEmbeddings` — Local, offline embedding via `sentence-transformers`

**Topics covered:**
- Generating embeddings for documents and queries
- Computing cosine similarity between embedding vectors
- Comparing embedding quality across models
- Understanding embedding dimensions and vector space

**Example — Cosine similarity between embeddings:**
```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vecs = embeddings.embed_documents(["cat", "dog", "automobile"])
sim = cosine_similarity([vecs[0]], [vecs[1]])
print(f"cat ↔ dog similarity: {sim[0][0]:.4f}")
```

---

### 🔟 Vector Stores

**Folder:** `10_Vector_Stores/`

Vector stores persist embeddings and enable efficient similarity search over large document collections. This module covers two of the most common vector store solutions used with LangChain.

**Stores explored:**
- **FAISS** — Facebook AI Similarity Search; fast, in-memory, local-first
- **Chroma** — Persistent, embedded vector database with metadata filtering

**Topics covered:**
- Creating vector stores from documents using `.from_documents()`
- Performing similarity search with `.similarity_search()`
- Persisting and reloading vector stores from disk
- Filtering results by metadata
- Comparing FAISS vs Chroma for different deployment needs

---

### 1️⃣1️⃣ Retrievers

**Folder:** `11_Retrievers/`

Retrievers are the interface layer between vector stores and chains — they accept a query string and return the most relevant documents. This module covers both standard and advanced retrieval strategies.

**Retrievers explored:**
- `VectorStoreRetriever` — Standard top-k similarity search
- `MMR (Maximal Marginal Relevance)` — Balances relevance with diversity to reduce redundant results
- `WikipediaRetriever` — Retrieves live content from Wikipedia articles

**Topics covered:**
- Configuring `search_type` and `search_kwargs` for fine-grained retrieval
- Using MMR to improve result diversity
- Integrating external knowledge sources as retrievers
- Plugging retrievers directly into RAG chains

---

### 1️⃣2️⃣ RAG (Retrieval Augmented Generation)

**Folder:** `12_Rag/`

A fully functional **Retrieval-Augmented Generation pipeline** — the complete integration of all previous components into a cohesive system that answers questions grounded in real document content.

**Topics covered:**
- End-to-end RAG: Load → Split → Embed → Store → Retrieve → Augment → Generate
- Building a modular RAG system across separate, reusable files
- Augmenting LLM prompts with retrieved context
- Querying a YouTube transcript knowledge base with natural language

**RAG Pipeline:**
```
[Load Document] → [Split into Chunks] → [Embed Chunks] → [Store in VectorDB]
                                                                ↓
[User Query] ─────────────────────────────────────→ [Retrieve Relevant Docs]
                                                                ↓
                                                     [Augment Prompt] → [LLM] → [Answer]
```

**Example — Full pipeline invocation:**
```python
transcript = get_youtube_transcript()
chunks = split_transcript_into_chunks(transcript)
vector_store = store_chunks_in_vectorstore(chunks)["vector_store"]

docs = retrieve_relevant_documents("What is the Golden Circle?", vector_store)
context = "\n\n".join([doc.page_content for doc in docs])
prompt = create_context_prompt().format(context=context, query=query)
answer = run_llm(prompt)
```

---

### 1️⃣3️⃣ Tool Calling

**Folder:** `13_Tool_Calling/`

Tool calling allows LLMs to invoke external functions — APIs, databases, calculators — and incorporate real-world results into their responses. This module implements a live currency converter as a practical demonstration.

**Topics covered:**
- Defining tools with the `@tool` decorator
- Binding tools to LLMs using `.bind_tools()`
- Parsing and executing `tool_calls` from model responses
- Using `InjectedToolArg` to pass arguments between dependent tool calls
- Building multi-step tool pipelines (fetch rate → calculate conversion)

**Example — Defining and binding a tool:**
```python
from langchain_core.tools import tool

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """Fetches the currency conversion factor between two currencies."""
    url = f"https://api.exchangerate.com/pair/{base_currency}/{target_currency}"
    return requests.get(url).json()

llm_with_tools = ChatGroq(model="llama-3.1-8b-instant").bind_tools([get_conversion_factor])
response = llm_with_tools.invoke([HumanMessage("Convert 10 USD to BDT")])
```

---

### 1️⃣4️⃣ AI Agents

**Folder:** `14_AI_Agents/`

AI Agents take autonomous action — using tools, reasoning about results, and iterating until a goal is reached. This module builds a **ReAct agent** powered by LangGraph and DuckDuckGo search.

**Topics covered:**
- Understanding the ReAct (Reasoning + Acting) loop
- Using `create_react_agent` from LangGraph's prebuilt utilities
- Integrating web search as a real-time knowledge tool
- Inspecting agent reasoning steps and intermediate outputs
- Combining LangChain tools with LangGraph agent orchestration

**ReAct Loop:**
```
[Reason] → (tool call) → [Search / Act] → [Reason] → ... → [Answer]
         ↘ (no tool needed) → [Answer directly]
```

**Example — ReAct agent with web search:**
```python
from langgraph.prebuilt import create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq

agent = create_react_agent(
    model=ChatGroq(model_name="llama-3.1-8b-instant"),
    tools=[DuckDuckGoSearchRun()]
)

response = agent.invoke({
    "messages": [{"role": "user", "content": "3 ways to reach Paris from London?"}]
})
print(response["messages"][-1].content)
```

---

### 🎨 Bonus: AI Storyteller

**Folder:** `AI-Storyteller/`

A full Streamlit web application that generates interactive, multi-chapter stories powered by LangChain and an LLM. Built as a capstone mini-project to demonstrate end-to-end LangChain application development.

**Features:**
- User-defined story genre, setting, and characters
- Chapter-by-chapter story generation with narrative continuity
- Conversation memory to maintain story context across chapters
- Clean, interactive Streamlit UI

**Run it locally:**
```bash
cd AI-Storyteller
streamlit run app.py
```

---

## ⚙️ Installation & Setup

**1. Clone this repository:**
```bash
git clone https://github.com/BrownSugar297/LangChain.git
cd LangChain
```

**2. Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Add your API keys to a `.env` file:**
```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
EXCHANGE_RATE_API_KEY=your_exchangerate_api_key_here
```

**5. Run any script:**
```bash
python 1_Chat_Models/openai_model.py
```

Or launch the AI Storyteller app:
```bash
cd AI-Storyteller && streamlit run app.py
```

---

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.11** | Core programming language |
| **LangChain** | LLM tooling, prompts, chains, and agent primitives |
| **LangChain-OpenAI** | OpenAI GPT model integration |
| **LangChain-Anthropic** | Anthropic Claude model integration |
| **LangChain-Google-GenAI** | Google Gemini model and embedding integration |
| **LangChain-Groq** | Groq LPU inference integration |
| **LangChain-HuggingFace** | Open-source model integration via Hugging Face |
| **LangChain-Community** | Community loaders, tools, and vector store wrappers |
| **LangGraph** | ReAct agent orchestration |
| **FAISS** | Fast in-memory vector similarity search |
| **ChromaDB** | Persistent embedded vector database |
| **Sentence Transformers** | Local embedding model inference |
| **Streamlit** | Web UI for the AI Storyteller project |
| **Pydantic v2** | Data validation and structured output schemas |
| **python-dotenv** | API key and environment management |

---

## 💡 Contribution

Contributions are always welcome! 🙌 If you'd like to improve this repository, add new LangChain examples, or fix issues:

**1. Fork the repository**

**2. Create a new branch for your feature or fix:**
```bash
git checkout -b feature/your-feature-name
```

**3. Commit your changes:**
```bash
git commit -m "Add: example for custom retriever with metadata filtering"
```

**4. Push to your fork:**
```bash
git push origin feature/your-feature-name
```

**5. Open a Pull Request** — describe what you've added and why it improves the repo.

---

> **Note:** This repository is a structured learning reference. Each folder is self-contained and can be explored independently. It is recommended to follow the numbered order for the best learning progression.

---

## 👨‍💻 Author

**Ashikur Rahman**
