from dotenv import load_dotenv
load_dotenv()  # Load all environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit App
st.set_page_config(page_title="Q&A Demo")

st.header("WELCOME TO PRANESH R'S CHATBOT")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User Input
input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and input_text:
    response = get_gemini_response(input_text)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
