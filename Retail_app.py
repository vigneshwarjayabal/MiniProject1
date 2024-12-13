import streamlit as st

st.title("Simple Streamlit App")

user_input = st.text_input("Enter your name:")

# Display a message when the user enters their name
if user_input:
    st.write(f"Hello, {user_input}!")
else:
    st.write("Please enter your name above.")
