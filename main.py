import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = 'sk-proj-JPVUMiURK1tUstXZ6ZdPT3BlbkFJtzqCGWlKCreutdYQroiF'

# Function to get response from OpenAI GPT-3.5
def get_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return str(e)

st.title("AI Chatbot")
st.write("Welcome! Type something to start the conversation.")

user_input = st.text_input("You: ")

if user_input:
    response = get_response(user_input)
    st.text_area("Chatbot:", value=response, height=200, max_chars=None, key=None)
