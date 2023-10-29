import streamlit as st

def main_page():
    st.title("Welcome to the EduBoost")

    # Only show the sidebar if the user is logged in
    if st.session_state.logged_in:
        with st.sidebar:
            st.write("Welcome to the EduBoost")
            # ... Your other sidebar content ...

def login_page():
    st.title("Login Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    api_key = st.text_input("API Key")  # Step 1: Adding API Key Input
    
    if st.button("Login"):
        # Predefined user credentials
        if username == "Alvin" and password == "123" and api_key:
            st.session_state.logged_in = True
            st.session_state.api_key = api_key  # Step 2: Store API Key in Session State
            st.success("Login Successful!")
            main_page()
        else:
            st.warning("Invalid Credentials")

if __name__ == '__main__':
    # Check if 'logged_in' key exists in session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        main_page()
    else:
        login_page()


