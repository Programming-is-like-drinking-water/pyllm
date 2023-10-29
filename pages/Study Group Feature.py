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
if 'announcements' not in st.session_state:
    st.session_state.announcements = {}

# Sidebar for creating and joining study groups and roles assignment
with st.sidebar:
    st.title("Study Group Feature")
    
    # Input for user's name
    st.session_state.username = st.text_input("Your Name", st.session_state.username)
    
    group_name = st.text_input("Enter Group Name")
    
    # Create group
    if st.button("Create Group"):
        if group_name and group_name not in st.session_state.groups:
            st.session_state.groups[group_name] = {'members': [], 'leader': None, 'teacher': None}
            st.session_state.current_group = group_name
            st.session_state.announcements[group_name] = []
            st.success(f"Group '{group_name}' created!")
        elif group_name in st.session_state.groups:
            st.warning(f"Group '{group_name}' already exists!")
        else:
            st.warning("Please enter a valid group name!")

    # Join group
    if st.button("Join Group"):
        if group_name in st.session_state.groups:
            if st.session_state.username not in st.session_state.groups[group_name]['members']:
                st.session_state.groups[group_name]['members'].append(st.session_state.username)
            st.session_state.current_group = group_name
            st.success(f"Joined group '{group_name}'!")
        else:
            st.warning("Group does not exist!")

    # Assign and remove roles if the group is selected
    if st.session_state.current_group:
        member_name = st.text_input("Enter Member Name for Role Assignment/Removal")
        role = st.radio("Assign/Remove Role", ["Member", "Leader", "Teacher"])
        if st.button("Assign Role"):
            if role == "Leader":
                st.session_state.groups[st.session_state.current_group]['leader'] = member_name
                st.success(f"{member_name} assigned as Leader!")
            elif role == "Teacher":
                st.session_state.groups[st.session_state.current_group]['teacher'] = member_name
                st.success(f"{member_name} assigned as Teacher!")
            else:
                if member_name not in st.session_state.groups[st.session_state.current_group]['members']:
                    st.session_state.groups[st.session_state.current_group]['members'].append(member_name)
                    st.success(f"{member_name} added as Member!")
        if st.button("Remove Role"):
            if role == "Leader" and st.session_state.groups[st.session_state.current_group]['leader'] == member_name:
                st.session_state.groups[st.session_state.current_group]['leader'] = None
                st.success(f"Leader role removed from {member_name}!")
            elif role == "Teacher" and st.session_state.groups[st.session_state.current_group]['teacher'] == member_name:
                st.session_state.groups[st.session_state.current_group]['teacher'] = None
                st.success(f"Teacher role removed from {member_name}!")

# Main content for displaying group members, roles and announcements
if st.session_state.current_group:
    st.title(f"Study Group: {st.session_state.current_group}")
    st.subheader("Announcements")
    announcement = st.text_input("New Announcement")
    if st.button("Post Announcement"):
        st.session_state.announcements[st.session_state.current_group].append(announcement)
        st.success("Announcement posted!")
    for ann in st.session_state.announcements[st.session_state.current_group]:
        st.info(ann)
    
    st.subheader("Members")
    for member in st.session_state.groups[st.session_state.current_group]['members']:
        role_str = " (Member)"
        if member == st.session_state.groups[st.session_state.current_group]['leader']:
            role_str = " (Leader)"
        elif member == st.session_state.groups[st.session_state.current_group]['teacher']:
            role_str = " (Teacher)"
        st.write(member + role_str)
else:
    st.write("Please create or join a group to see its details.")
