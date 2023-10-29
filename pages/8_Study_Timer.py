import streamlit as st
import time

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

def timer_page():
    st.title("📝 Study Timer")

    # Check if the timer has started
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    if "end_time" not in st.session_state:
        st.session_state.end_time = None
    if "running" not in st.session_state:
        st.session_state.running = False

    # Display timer
    if st.session_state.running:
        elapsed_time = int(time.time() - st.session_state.start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        st.write(f"Time Elapsed: {minutes} minutes {seconds} seconds")
    else:
        st.write("Click 'Start' to begin timing your study session.")

    # Display "Start" button and handle logic
    start_clicked = st.button("Start")
    if start_clicked and not st.session_state.running:
        st.session_state.start_time = time.time()
        st.session_state.running = True

    # Display "End" button and handle logic
    end_clicked = st.button("End")
    if end_clicked and st.session_state.running:
        st.session_state.end_time = time.time()
        st.session_state.running = False
        elapsed_time = int(st.session_state.end_time - st.session_state.start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        st.success(f"You've studied for {minutes} minutes and {seconds} seconds!")
        if st.button("Confirm"):
            st.session_state.start_time = None
            st.session_state.end_time = None

    # Display "Refresh" button and handle logic
    if st.button("Refresh"):
        st.experimental_rerun()

timer_page()
