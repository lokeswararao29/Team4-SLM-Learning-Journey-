import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def read_resume(file):
    pdf = PdfReader(file)
    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    return text


st.title("Resume RAG Chatbot")

uploaded_file = st.file_uploader(
    "Upload Your Resume PDF",
    type="pdf"
)


if uploaded_file:

    resume_text = read_resume(uploaded_file)

    st.success("Resume uploaded successfully!")

    question = st.text_input(
        "Ask a question about your resume"
    )

    if question:

        prompt = f"""
        You are a resume assistant.

        Resume:
        {resume_text}

        Question:
        {question}

        Answer the question based only on the resume.
        """

        response = model.generate_content(prompt)

        st.write("Answer:")
        st.write(response.text)