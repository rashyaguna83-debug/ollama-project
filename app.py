import streamlit as st
import requests

st.title("🤖 Python AI Assistant")

prompt = st.text_input("Enter your question:")

if st.button("Generate"):
    if prompt:
        url = "http://localhost:11434/api/generate"

        data = {
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()
            st.subheader("AI Response")
            st.write(result["response"])
        else:
            st.error("Error connecting to Ollama")
    else:
        st.warning("Please enter a question.")
