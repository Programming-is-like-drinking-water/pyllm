import streamlit as st
from langchain.llms import OpenAI

if 'api_key' not in st.session_state:
    st.session_state.api_key = None
if 'api_key' in st.session_state:
    openai_api_key = st.session_state.api_key
try:
    openai_api_key = st.session_state.api_key
except KeyError:
    st.warning("API key not initialized.")

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

def generate_response(sentence):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    return llm(sentence)

st.title("🦜🔗 Personalize Learning Plan")

with st.form("myform"):
    topics = ["Math", "English", "Science", "History"]
    selected_topic = st.selectbox("Choose a topic:", topics)
    
    number = st.number_input("Enter a number", value=0)
    
    selected_date = st.date_input("Select a date")
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        sentence = f"I want {selected_topic}，get to {number} before {selected_date}."
        response = generate_response(sentence)
        st.write("OpenAI Response:", response)


