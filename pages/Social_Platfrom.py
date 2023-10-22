import streamlit as st

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

# Simulating a database using lists (just for demonstration purposes)
posts = []
comments = {}
likes = {}
user_profile = {"username": "JohnDoe", "bio": ""}

def display_feed():
    # Display the feed with posts, comments, and likes
    for idx, post in enumerate(posts):
        st.text_area("Post", post, height=100, key=f"post_{idx}")
        if st.button("Like", key=f"like_btn_{idx}"):
            likes[idx] = likes.get(idx, 0) + 1
        st.write(f"Likes: {likes.get(idx, 0)}")
        user_comment = st.text_input("Add a comment", key=f"comment_{idx}")
        if st.button("Submit Comment", key=f"submit_comment_{idx}"):
            comments[idx] = comments.get(idx, []) + [user_comment]

        for comment in comments.get(idx, []):
            st.text_area("Comment", comment, height=50, key=f"comment_text_{idx}")

def display_profile():
    # Display the user profile and settings
    st.subheader("Profile")
    user_profile["username"] = st.text_input("Username", user_profile["username"])
    user_profile["bio"] = st.text_area("Bio", user_profile["bio"])
    if st.button("Save Profile"):
        st.success("Profile updated!")

# App layout
st.title("Social Platform Demo")

menu = ["Feed", "Profile"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Feed":
    st.subheader("Create a Post")
    new_post = st.text_area("What's on your mind?")
    if st.button("Post"):
        posts.append(new_post)
    display_feed()
elif choice == "Profile":
    display_profile()