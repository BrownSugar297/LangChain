import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768",
]

st.set_page_config(
    page_title="FairyTale AI",
    page_icon="🌈",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    border-right: 1px solid #e6e6e6;
}
h1, h2, h3 {
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.title("🌈 Kids Story Wizard")
st.caption("Simple, safe, and fun AI stories for kids")
st.divider()

with st.sidebar:
    st.header("⚙️ Story Settings")

    genre = st.selectbox(
        "Choose Story World",
        [
            "🚀 Space Adventure",
            "🐶 Talking Animals",
            "🌲 Magic Forest",
            "🤖 Friendly Robots"
        ]
    )

    story_type = st.radio(
        "Story Length",
        ["Short Story", "Long Story"]
    )


def is_quota_error(e: Exception) -> bool:
    msg = str(e).lower()
    return "429" in msg or "rate_limit" in msg or "quota" in msg


def get_ai_response(user_topic, story_genre, length_type):

    if length_type == "Short Story":
        count_rule = "exactly 4 to 5 sentences"
        max_tokens = 200
    else:
        count_rule = "exactly 10 to 12 sentences"
        max_tokens = 600

    template = """
    You are a professional children's storyteller.
    Write a {genre} story about {topic}.

    Rules:
    1. Length: The story must be {count_rule}. Count carefully.
    2. Language: Simple, kind, and fun for kids aged 4-8.
    3. Ending: Always finish with a happy ending and a complete sentence.
    4. Crucial: Do not stop in the middle of a sentence!
    """

    prompt = PromptTemplate.from_template(template)

    for i, model_name in enumerate(MODELS):
        try:
            llm = ChatGroq(
                model=model_name,
                api_key=API_KEY,
                temperature=0.7,
                max_tokens=max_tokens,
            )
            chain = prompt | llm
            result = chain.invoke({
                "genre": story_genre,
                "topic": user_topic,
                "count_rule": count_rule
            })
            return result

        except Exception as e:
            if is_quota_error(e):
                if i < len(MODELS) - 1:
                    continue  
                else:
                    raise Exception("ALL_QUOTA_EXCEEDED")
            else:
                raise e

    raise Exception("ALL_QUOTA_EXCEEDED")


if topic := st.chat_input("Enter a name or object to start the magic..."):

    with st.chat_message("user"):
        st.write(topic)

    with st.chat_message("assistant"):

        if not API_KEY:
            st.error("❌ Missing API Key! Please add GROQ_API_KEY to your .env file.")
            st.code("GROQ_API_KEY=your_key_here", language="bash")

        else:
            with st.spinner("🪄 Creating your magical story..."):
                try:
                    response = get_ai_response(topic, genre, story_type,)
                    st.write(response.content)
                    st.balloons()

                except Exception as e:
                    if "ALL_QUOTA_EXCEEDED" in str(e):
                        st.warning("⏳ Daily limit reached for all models!")
                        st.info("💡 Quota resets in 24 hours. Come back tomorrow!")
                    else:
                        st.error("Something went wrong. Please try again!")
                        st.exception(e)

st.divider()
st.caption("Built with LangChain & Groq | Safe AI for Kids")