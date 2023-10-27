import streamlit as st
from datetime import datetime

# Check if the user is logged in
if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

# Simulating a database using lists (just for demonstration purposes)
posts = st.session_state.get("posts", [])
timestamps = st.session_state.get("timestamps", [])
likes = st.session_state.get("likes", {})
comments = st.session_state.get("comments", {})

def create_post():
    st.title("🔗 Create Post")
    new_post = st.text_area("Write a new post", "Anything want to share?")
    if st.button("Submit Post"):
        if new_post != "Anything want to share?":
            posts.append(new_post)
            timestamps.append(datetime.now())
            st.session_state["posts"] = posts
            st.session_state["timestamps"] = timestamps
            st.success("Submit Success")

def view_posts():
    st.title("🔗 View Posts")
    sorted_indices = sorted(range(len(timestamps)), key=lambda i: timestamps[i], reverse=True)
    for idx in sorted_indices:
        st.write("----")
        st.markdown(f"**{posts[idx]}**")
        st.markdown(f"<span style='color: gray;'>{timestamps[idx].strftime('%d/%m/%Y %H:%M')}</span>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            if st.button("Like", key=f"like_btn_{idx}"):
                toggle_like(idx)
        with col2:
            st.write(likes.get(idx, 0))
        with col3:
            if st.button("Comment", key=f"comment_btn_{idx}"):
                user_comment = st.text_input("Write a comment", key=f"comment_input_{idx}")
                if st.button("Submit Comment", key=f"submit_comment_{idx}"):
                    comments[idx] = comments.get(idx, []) + [user_comment]
                    st.session_state["comments"] = comments
                    st.experimental_rerun()
        for comment in comments.get(idx, []):
            st.text(f"Comment: {comment}")

def toggle_like(idx):
    liked = st.session_state.get(f"liked_{idx}", False)
    if liked:
        likes[idx] -= 1
    else:
        likes[idx] = likes.get(idx, 0) + 1
    st.session_state[f"liked_{idx}"] = not liked
    st.session_state["likes"] = likes

menu = st.sidebar.selectbox("Choose an option", ["Create Post", "View Posts"])
if menu == "Create Post":
    create_post()
elif menu == "View Posts":
    view_posts()
