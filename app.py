import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="My Simple Website",
    page_icon="👋",
    layout="wide"
)

# Add a title
st.title("Welcome to My Simple Website")

# Add some text
st.write("This is my first Streamlit app!")

# Add a sidebar
st.sidebar.title("Navigation")

# Add interactive elements
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

# Add buttons
if st.button("Click me!"):
    st.balloons()