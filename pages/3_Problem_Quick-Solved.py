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
# openai_api_key = st.session_state.api_key

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

st.title("🦜 Problem Quick-Solved")

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What problems do you need to solve?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text)
