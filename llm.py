import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash-lite")

def ask_llm(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"



question = st.text_input("Enter your question")

if st.button("Ask AI"):
    if question:
        answer = rag_query(df, question, ask_llm)
        st.write("### AI Answer")
        st.write(answer)



import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def ask_llm(question):
    response = model.generate_content(question)
    return response.text