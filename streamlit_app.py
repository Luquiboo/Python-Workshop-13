import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎈 My new Streamlit app!!!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)



pd.read_csv("https://raw.githubusercontent.com/LUCE-Blockchain/Databases-for-teaching/refs/heads/main/Framingham%20Dataset.csv")
cvd = pd.read_csv("https://raw.githubusercontent.com/LUCE-Blockchain/Databases-for-teaching/refs/heads/main/Framingham%20Dataset.csv")

st.write(cvd.head())


if st.button("Doctor am I going to be okay?"):
    st.write("### You are going to die")

if st.button("Help!"):
    st.write("#### L")

if st.button("I smoke"):
    st.write("### You are going to die")

if st.button("I'm hypertensive"):
    st.write("### You are going to die")

if st.button("I'm tachycardic"):
    st.write("### You are going to die")

st.button("Goodbye")
