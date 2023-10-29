import streamlit as st

# Check if the user is logged in
if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

# Initialize session state variables
if 'groups' not in st.session_state:
    st.session_state.groups = {}
if 'current_group' not in st.session_state:
    st.session_state.current_group = None
if 'username' not in st.session_state:
    st.session_state.username = ""

# Sidebar for creating and joining study groups
with st.sidebar:
    st.title("Study Group Feature")
    
    # Input for user's name
    st.session_state.username = st.text_input("Your Name", st.session_state.username)
    
    group_name = st.text_input("Enter Group Name")
    if st.button("Create Group"):
        if group_name and group_name not in st.session_state.groups:
            st.session_state.groups[group_name] = []
            st.session_state.current_group = group_name
            st.success(f"Group '{group_name}' created!")
        elif group_name in st.session_state.groups:
            st.warning(f"Group '{group_name}' already exists!")
        else:
            st.warning("Please enter a valid group name!")

    if st.button("Join Group"):
        if group_name in st.session_state.groups:
            if st.session_state.username not in st.session_state.groups[group_name]:
                st.session_state.groups[group_name].append(st.session_state.username)
            st.session_state.current_group = group_name
            st.success(f"Joined group '{group_name}'!")
        else:
            st.warning("Group does not exist!")

# Main content for displaying group members
if st.session_state.current_group:
    st.title(f"Members of {st.session_state.current_group}")
    for member in st.session_state.groups[st.session_state.current_group]:
        st.write(member)
else:
    st.write("Please create or join a group to see its members.")
