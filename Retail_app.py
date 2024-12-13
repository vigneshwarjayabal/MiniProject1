import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Create a text input field for user input
user_input = st.text_input("Enter your name:")

# Display a message when the user enters their name
if user_input:
    st.write(f"Hello, {user_input}!")
else:
    st.write("Please enter your name above.")
