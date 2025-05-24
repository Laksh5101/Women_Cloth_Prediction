---
title: Women Clothing Sentiment Predictor
emoji: 👗
colorFrom: pink
colorTo: red
sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
pinned: false
---

# 👗 Women Clothing Review Sentiment Predictor  

An intuitive, AI-powered web app that analyzes customer reviews on women’s clothing to predict **sentiment** — whether a review is **positive** or **negative**. Built with machine learning and Streamlit, this project is ideal for showcasing data science and NLP capabilities.

---

## 📋 Project Overview  

This application serves as a **product review analyzer** for e-commerce or retail clothing platforms. It enables businesses and analysts to:  
- Understand customer sentiment at scale  
- Gain insights from reviews automatically  
- Prioritize product improvements based on feedback tone  

---

## 🔑 Features  

### ✨ Review Sentiment Analysis  
- Accepts user-written reviews as input  
- Uses a trained ML model to classify sentiment  
- Displays result as either 😊 **Positive** or ☹️ **Negative**

### 🔎 Missing Review Handling  
- Automatically fills in missing reviews with a neutral placeholder  
- Ensures robustness even with incomplete data

---

## 🛠️ Tech Stack  

| **Component**       | **Technology**                        |  
|---------------------|----------------------------------------|  
| **Frontend**        | [Streamlit](https://streamlit.io/)     |  
| **Backend**         | Python                                 |  
| **Modeling**        | `scikit-learn`, `TfidfVectorizer`      |  
| **Data Handling**   | `pandas`, `numpy`                      |  
| **Model Deployment**| `pickle` for model serialization       |  

---

## 📊 How It Works  

1. **Preprocessing**  
   - Handles missing or empty reviews using `pandas`  
   - Applies TF-IDF vectorization to convert text to numerical features  

2. **Model Prediction**  
   - Loads a pre-trained sentiment classification model  
   - Classifies reviews into positive or negative based on learned patterns  

3. **User Interface**  
   - Allows users to input a review  
   - Displays the sentiment prediction in a friendly UI  

---

## 🙌 Contributing  

Contributions are welcome! Help improve the prediction model, add new features, or enhance the UI.

1. **Fork** the repository  
2. **Create a feature branch**  
3. **Submit a pull request** with your improvements  

