import streamlit as st
from langchain.llms import OpenAI

openai_api_key = st.session_state.api_key

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/2_Chat_with_search.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

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


