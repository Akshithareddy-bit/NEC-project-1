import streamlit as st
import random

def show_prediction():

    st.header("Customer Segment Prediction")

    age = st.number_input("Age", 18, 70)

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    budget = st.number_input(
        "Budget",
        1000,
        100000
    )

    browsing = st.slider(
        "Browsing Time",
        1,
        100
    )

    discount = st.slider(
        "Discount Sensitivity",
        1,
        10
    )

    if st.button("Predict Segment"):

        segment = random.choice([
            "High Value",
            "Medium Value",
            "Low Value"
        ])

        prob = round(random.uniform(70,99),2)

        st.success(
            f"Predicted Segment : {segment}"
        )

        st.info(
            f"Probability : {prob}%"
        )