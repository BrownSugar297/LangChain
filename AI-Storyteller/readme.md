### 🎨 AI Storyteller:

A complete **mini-project** built using LangChain components and deployed as an interactive **Streamlit** web application. The AI Storyteller generates creative, engaging stories based on user-provided prompts, genre, and tone preferences.

**Features:**
- Genre selection (Fantasy, Sci-Fi, Mystery, Romance, Horror)
- Tone control (Humorous, Dark, Adventurous, Emotional)
- Adjustable story length via token control
- Streaming output for real-time story generation
- Clean, minimal Streamlit UI

**Pipeline:**
```
User Input (Streamlit) → ChatPromptTemplate → ChatOpenAI (streaming) → StrOutputParser → Streamlit UI
```

**Run the project:**
```bash
streamlit run AI-Storyteller/app.py
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
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

**5. Run any notebook:**
```bash
jupyter notebook
```
Navigate to the relevant module folder and open the `.ipynb` file. Folders are numbered in the recommended learning order.

---

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.11** | Core programming language |
| **LangChain** | Core framework for LLM pipelines |
| **LangChain-Core** | Runnables, prompts, parsers, base abstractions |
| **LangChain-OpenAI** | OpenAI GPT model and embedding integration |
| **LangChain-Anthropic** | Anthropic Claude model integration |
| **LangChain-Google-GenAI** | Google Gemini model integration |
| **LangChain-Groq** | Groq LPU fast inference integration |
| **LangChain-HuggingFace** | Open-source Hugging Face model integration |
| **LangChain-Community** | Community loaders, tools, and integrations |
| **OpenAI API** | GPT-4 / GPT-4-turbo language and embedding models |
| **Anthropic API** | Claude 3 language models |
| **Google Generative AI** | Gemini models |
| **Groq** | Fast inference for open-source LLMs |
| **HuggingFace Hub + Transformers** | Open-source model hosting and inference |
| **FAISS** | Fast local vector similarity search |
| **ChromaDB** | Lightweight open-source vector store |
| **sentence-transformers** | Open-source embedding models |
| **PyMuPDF / pdfplumber / PyPDF** | PDF document loading and text extraction |
| **scikit-learn** | Cosine similarity computation |
| **Streamlit** | Web UI for the AI Storyteller mini-project |
| **LangGraph** | Agent workflow orchestration |
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
git commit -m "Add: semantic chunking example in Text Splitters module"
```

**4. Push to your fork:**
```bash
git push origin feature/your-feature-name
```

**5. Open a Pull Request** — describe what you've added and why it improves the repo.

---

> **Note:** This repository is a structured learning reference. Each folder is self-contained and can be explored independently. Following the numbered order (1 → 14) provides the most logical and progressive learning experience, as each module builds on concepts from the previous ones.
