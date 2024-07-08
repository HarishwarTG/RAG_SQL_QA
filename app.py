import streamlit as st
from src.Langchain_model import get_answer_to_question

st.set_page_config(layout="centered", page_title="Walmart Inventory Q&A", page_icon="🏪")

c1, c2 = st.columns([0.32, 2])

with c1:
    st.image( "images/logo.png", width=85)
with c2:
    st.caption("")
    st.title("Walmart Inventory Q&A")

st.sidebar.markdown("---")

st.sidebar.write(
    """
    Streamlit Q&A created by [Harishwar T G](https://www.linkedin.com/in/harishwartg/).

    This project utilizes GooglePalm LLM, Langchain, HuggingFace's Embedding model, and FAISS Vectorstore.

    For more details, please visit the [GitHub repository](link-to-repo).

    **Note:** This is a personal learning project and does not include the original inventory database.
    """
)


st.write("Ask questions about the Walmart store database.")

question = st.text_input("Enter your question:")
if st.button("Get Answer"):
    if question:
        with st.spinner("Searching through inventory..."):
            answer = get_answer_to_question(question)
            st.write(answer)
    else:
        st.error("Please enter a question.")