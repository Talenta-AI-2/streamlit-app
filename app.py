# app.py
import streamlit as st

# Simple rule-based chatbot logic
def get_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a bunch of code, but thanks for asking! How can I help you?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

st.title("Simple Chatbot")
st.write("Welcome! Type something to start the conversation.")

user_input = st.text_input("You: ")

if user_input:
    response = get_response(user_input)
    st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=None)