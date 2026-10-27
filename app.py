
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.title("My Simple AI Chatbot")

if not api_key:
    st.error("API key not found in .env file")
else:
    client = genai.Client(api_key=api_key)

    question = st.text_input("Ask your question")

    if st.button("Send"):
        if question:
            try:
                with st.spinner("AI is thinking..."):
                    response = client.interactions.create(
                        model="gemini-3.8-flash",
                        input=question
                    )

                st.write(response.output_text)

            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a question")
