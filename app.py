import streamlit as st
from utils.data_loader import load_data
from utils.llm import ask_llm
from utils.rag import rag_query
from utils.viz import plot_chart

st.set_page_config(page_title="AI Copilot Pro", layout="wide")

st.title("🤖 AI Copilot Pro (Gemini + CSV + RAG)")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.success("Data Loaded Successfully!")
    st.dataframe(df)

    st.subheader("📊 Visualization")
    fig = plot_chart(df)
    if fig:
        st.pyplot(fig)
    else:
        st.warning("Not enough numeric columns for graph")

    st.subheader("💬 Ask AI about your data")

    question = st.text_input("Enter your question")

    if question:
        answer = rag_query(df, question, ask_llm)
        st.write("### AI Answer")
        st.write(answer)

else:
    st.info("Please upload a CSV file")

import streamlit as st
from utils.llm import ask_llm

st.title("AI Copilot Pro")

question = st.text_input("Enter your question")

if question:
    answer = ask_llm(question)
    st.write(answer)