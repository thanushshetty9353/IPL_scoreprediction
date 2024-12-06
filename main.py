import streamlit as st
from predictor import predictRuns
import pandas as pd

st.title("IPL Score Prediction")
st.write("This app predicts the score based on preprocessed input data.")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    file_path = "uploaded_data.csv"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("Uploaded file contents:")
    data = pd.read_csv(file_path)
    st.write(data.head())

    predicted_score = predictRuns(file_path)
    st.write("PREDICTED SCORE IS: ", predicted_score)
