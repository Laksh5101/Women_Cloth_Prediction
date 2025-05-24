import streamlit as st
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
try:
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('vectorizer.pkl', 'rb') as vectorizer_file:
        tfidf = pickle.load(vectorizer_file)
except FileNotFoundError:
    st.error("Model or vectorizer file not found. Please ensure 'model.pkl' and 'vectorizer.pkl' are present in the directory.")
    st.stop()

# App title
st.set_page_config(page_title="Clothing Review Sentiment Predictor")
st.title("🛍️ Women Clothing Review Sentiment Predictor")

st.markdown("""
This app predicts whether a review on women’s clothing is **positive** or **negative** using a machine learning model trained on clothing review data.
""")

# Text input
review = st.text_area("✍️ Enter your clothing review below:", height=150)

# Prediction button
if st.button("🔍 Predict Sentiment"):
    if review.strip() == "":
        st.warning("⚠️ Please enter a review before predicting.")
    else:
        # Transform and predict
        review_transformed = tfidf.transform([review])
        prediction = model.predict(review_transformed)
        sentiment = "😊 Positive" if prediction[0] == 1 else "☹️ Negative"

        st.success(f"Predicted Sentiment: {sentiment}")
