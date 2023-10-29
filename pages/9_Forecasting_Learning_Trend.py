import streamlit as st
import openai
import re
from PyPDF2 import PdfReader
from io import BytesIO

openai.api_key = st.session_state.api_key
# from config import API_KEY

# openai.api_key = API_KEY
# Initialize OpenAI API
# openai.api_key = "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"
# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/2_Chat_with_search.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

def analyze_student_performance(text):
    # text follows a certain pattern "Subject: Grade"
    grades = re.findall(r'(.*?):\s*(\w+)', text)
    subjects = {subject: grade for subject, grade in grades}

    prompt = f"Based on the grade report of the student in the following subjects:\n"
    prompt += "\n".join([f"{subject}: {grade}" for subject, grade in subjects.items()])
    prompt += "\nPlease analyze the student's academic performance, give recommendations, and predict future impacts. Also, write a plan for improving the corresponding subject."
    # prompt += "\nPlease analyze the student's academic performance and predict future impacts."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300
    )

    analysis = response.choices[0].text.strip()
    return analysis

# UI components
uploaded_file = st.file_uploader("Upload the student's grade PDF", type=["pdf"])

if uploaded_file:
    with BytesIO(uploaded_file.read()) as byte_io:
        pdf_reader = PdfReader(byte_io)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()

    # Analyze student's academic situation and future impacts
    analysis = analyze_student_performance(text)
    st.write("Analysis, Recommendations and Predictions")
    st.write(analysis)
