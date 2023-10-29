import openai
import streamlit as st

openai_api_key = st.session_state.api_key

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()
# Initialization
st.title("📝 Generate Chat Report")

# Hardcoded OpenAI API key (please replace with your actual key)
# openai_api_key = "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"  # Replace with your actual OpenAI API Key

if "messages" not in st.session_state:
    st.session_state.messages = []

messages = st.session_state.messages

# Generate Report Button Functionality
if st.button("Generate Report"):
    report_question = "Can you help me summarize everything I asked?IF NOT,give answer' no record'"
    messages.append({"role": "user", "content": report_question})

    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    report_response = response.choices[0].message.content if response.choices[0].message.content else "No record"
    with st.chat_message("assistant"):
        messages.append({"role": "assistant", "content": report_response})
        st.write(report_response)
