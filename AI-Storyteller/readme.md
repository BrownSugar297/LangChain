🎨 AI Storyteller

A complete mini-project built using LangChain components and deployed as an interactive Streamlit web application. The AI Storyteller generates creative, engaging stories based on user-provided prompts, genre, and tone preferences.
Features:

Genre selection (Fantasy, Sci-Fi, Mystery, Romance, Horror)
Tone control (Humorous, Dark, Adventurous, Emotional)
Adjustable story length via token control
Streaming output for real-time story generation
Clean, minimal Streamlit UI

Pipeline:
User Input (Streamlit) → ChatPromptTemplate → ChatOpenAI (streaming) → StrOutputParser → Streamlit UI
Run the project:
bashstreamlit run AI-Storyteller/app.py

⚙️ Installation & Setup
1. Clone this repository:
bashgit clone https://github.com/BrownSugar297/LangChain.git
cd LangChain
2. Create and activate a virtual environment:
bashpython -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
3. Install dependencies:
bashpip install -r requirements.txt
4. Add your API keys to a .env file:
envOPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
5. Run any notebook:
bashjupyter notebook
Navigate to the relevant module folder and open the .ipynb file. Folders are numbered in the recommended learning order.

🧰 Technologies Used
TechnologyPurposePython 3.11Core programming languageLangChainCore framework for LLM pipelinesLangChain-CoreRunnables, prompts, parsers, base abstractionsLangChain-OpenAIOpenAI GPT model and embedding integrationLangChain-AnthropicAnthropic Claude model integrationLangChain-Google-GenAIGoogle Gemini model integrationLangChain-GroqGroq LPU fast inference integrationLangChain-HuggingFaceOpen-source Hugging Face model integrationLangChain-CommunityCommunity loaders, tools, and integrationsOpenAI APIGPT-4 / GPT-4-turbo language and embedding modelsAnthropic APIClaude 3 language modelsGoogle Generative AIGemini modelsGroqFast inference for open-source LLMsHuggingFace Hub + TransformersOpen-source model hosting and inferenceFAISSFast local vector similarity searchChromaDBLightweight open-source vector storesentence-transformersOpen-source embedding modelsPyMuPDF / pdfplumber / PyPDFPDF document loading and text extractionscikit-learnCosine similarity computationStreamlitWeb UI for the AI Storyteller mini-projectLangGraphAgent workflow orchestrationpython-dotenvAPI key and environment management

💡 Contribution
Contributions are always welcome! 🙌 If you'd like to improve this repository, add new LangChain examples, or fix issues:
1. Fork the repository
2. Create a new branch for your feature or fix:
bashgit checkout -b feature/your-feature-name
3. Commit your changes:
bashgit commit -m "Add: semantic chunking example in Text Splitters module"
4. Push to your fork:
bashgit push origin feature/your-feature-name
5. Open a Pull Request — describe what you've added and why it improves the repo.
