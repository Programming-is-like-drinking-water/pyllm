import streamlit as st
import openai
from difflib import SequenceMatcher

if 'api_key' not in st.session_state:
    st.session_state.api_key = None
if 'api_key' in st.session_state:
    openai.api_key = st.session_state.api_key
try:
    openai.api_key = st.session_state.api_key
except KeyError:
    st.warning("API key not initialized.")

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

st.title("📝 Smart Exercise Bank with Auto-Grading and Feedback")

# Initialize session state
if "questions" not in st.session_state:
    st.session_state.questions = []
if "student_answers" not in st.session_state:
    st.session_state.student_answers = {}

# Function to generate open-ended questions based on a topic
def generate_questions(topic):
    prompt = f"Generate 2 open-ended questions about {topic}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
    )
    questions = response.choices[0].text.strip().split("\n")
    st.session_state.questions = questions

# Function to calculate similarity between two strings
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Topic selection and question generation
topic = st.text_input("Enter the topic you want to study:")
if st.button("Generate Questions"):
    generate_questions(topic)

# Display questions and collect answers
if st.session_state.questions:
    st.write("### Questions:")
    for idx, question in enumerate(st.session_state.questions):
        st.write(f"{idx+1}. {question}")
        st.session_state.student_answers[idx] = st.text_input(f"Your answer for question {idx+1}:", key=idx)

# Auto-grading
if st.button("Submit for Auto-Grading"):
    total_score = 0
    st.write("### Grading Results")
    for idx, question in enumerate(st.session_state.questions):
        # Generate a sample correct answer for the question
        prompt = f"What could be a correct answer for the following question?\n{question}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,
        )
        correct_answer = response.choices[0].text.strip()

        # Compare the student's answer with the correct answer
        student_answer = st.session_state.student_answers[idx]
        score = similarity(student_answer, correct_answer)

        # Explain the grading
        st.write(f"**Question {idx+1}**: {question}")
        st.write(f"Your answer: {student_answer}")
        st.write(f"Sample correct answer: {correct_answer}")
        st.write(f"Similarity score: {score:.2f}")
        if score >= 0.8:
            st.write("Status: Correct")
            total_score += 1
        else:
            st.write("Status: Incorrect")
        
    st.write(f"Your total score is {total_score} out of {len(st.session_state.questions)}.")
