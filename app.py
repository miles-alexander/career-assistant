import streamlit as st
import os
from openai import OpenAI

client = OpenAI()
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# set Streamlit app title
st.title("Career Assistant Chatbot 💼💰📈")

# set fine-tuned model ID
FINE_TUNED_MODEL = "ft:gpt-3.5-turbo-0125:personal::AzCXzj45"

# initialize session state for messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history
for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "🤖" 
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# handle user input
if prompt := st.chat_input("Ask me about career development!"):
    # add user's message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # display user's message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # call fine-tuned model
    with st.chat_message("assistant", avatar="🤖"):
        stream = client.chat.completions.create(model=FINE_TUNED_MODEL,
        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
        stream=True)
        response = st.write_stream(stream)

    # store assistant's response
    st.session_state.messages.append({"role": "assistant", "content": response})
