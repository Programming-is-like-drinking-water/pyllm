import streamlit as st
import openai
import re
from PyPDF2 import PdfReader
from io import BytesIO

openai.api_key = st.session_state.api_key

# import os
# os.environ["API_KEY"] = st.session_state.api_key

# from config import API_KEY

# openai.api_key = API_KEY

# Initialize OpenAI API
# openai.api_key = "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"
# with st.sidebar:
#     openai.api_key = st.text_input("OpenAI API Key",type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/2_Chat_with_search.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

def fetch_answers_from_api(question_list):
    questions_joined = "\n".join([f"Q{i+1}: {q}" for i, q in enumerate(question_list.values())])
    prompt = f"Please write the numerical answers directly for the following computational questions:\n{questions_joined}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )

    answers_text = response.choices[0].text.strip()
    answer_list = re.findall(r"Q(\d+):\s*(\d+)", answers_text)
    standard_answers = {f"Q{index}": int(ans) for index, ans in answer_list}

    return standard_answers

def score_answers(student_answers, standard_answers):
    score = 0
    for q, student_ans in student_answers.items():
        if student_ans == standard_answers.get(q, None):
            score += 1
    return score

# Fetching the PDF and extracting text
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    with BytesIO(uploaded_file.read()) as byte_io:
        pdf_reader = PdfReader(byte_io)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()

    questions_found = re.findall(r'(Q\d+):\s*(.*?)\s*ANS:\s*(\d+)', text)
    student_answers = {q: int(ans) for q, _, ans in questions_found}
    question_list = {q: question for q, question, _ in questions_found}

    standard_answers = fetch_answers_from_api(question_list)
    st.write("Standard Answers")
    st.write(standard_answers)

    final_score = score_answers(student_answers, standard_answers)
    st.write("Final Score")
    st.write(final_score)

