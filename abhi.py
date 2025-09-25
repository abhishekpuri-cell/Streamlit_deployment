import streamlit as st

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Simple LLM-Powered Chatbot")

# Define the fixed answer
FIXED_RESPONSE = "I am a small demo chatbot. I give the same answer to every question!"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! Ask me anything."}
    ]

# Display messages
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Input box
if prompt := st.chat_input("Type your question..."):
    # Save user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Bot always replies with the fixed response
    st.session_state["messages"].append({"role": "assistant", "content": FIXED_RESPONSE})
    st.chat_message("assistant").markdown(FIXED_RESPONSE)
