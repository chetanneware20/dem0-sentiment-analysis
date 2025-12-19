import streamlit as st
from transformers import pipeline

# Page config
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="😊",
    layout="centered"
)

# Title
st.title("Sentiment Analysis using Transformers")
st.write("Enter a sentence and analyze its sentiment.")

# Load model (cached to avoid reloading)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# User input
text = st.text_area("Enter text:", placeholder="I don't like this product")

# Predict button
if st.button("Analyze Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        result = model(text)[0]
        label = result["label"]
        score = result["score"]

        if label == "POSITIVE":
            st.success(f"😊 Sentiment: {label}")
        else:
            st.error(f"😠 Sentiment: {label}")

        st.write(f"**Confidence:** {score:.4f}")
