import google.generativeai as genai
import os
import streamlit as st

# Replace with your actual API key
genai.configure(api_key="************Ap-Oj3hidtBqs1LLM3MT0Ml7Bhc")
model = genai.GenerativeModel("gemini-pro")

def generate_article(topic, tone="informative", length="medium"):
    """Generates an article using the Gemini API.

    Args:
        topic: The topic of the article.
        tone: The desired tone of the article (e.g., "informative", "persuasive", "humorous").
        length: The desired length of the article (e.g., "short", "medium", "long").

    Returns:
        The generated article as a string, or an error message if generation fails.
    """

    try:
        completion = model.generate_content(
            f"Write an article about {topic}. The tone should be {tone} and the length should be {length}.",
        )

        return completion.text
    except Exception as e:
        return f"An error occurred: {e}"

st.title("Article Generator")

topic = st.text_input("Enter the article topic:")
tone = st.selectbox("Select the desired tone:", ["informative", "persuasive", "humorous", "formal", "informal"])
length = st.selectbox("Select the desired length:", ["short", "medium", "long"])

if st.button("Generate Article"):
    if topic:
        article = generate_article(topic, tone, length)
        st.write(article)
    else:
        st.warning("Please enter a topic.")

