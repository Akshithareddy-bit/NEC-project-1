import streamlit as st
import pandas as pd
import plotly.express as px

def show_churn():

    st.header("Customer Churn Analysis")

    df = pd.read_csv(
        "data/customer_dataset.csv"
    )

    churn_rate = (
        df["Churn"].mean()*100
    )

    st.metric(
        "Churn Rate",
        f"{churn_rate:.2f}%"
    )

    fig = px.pie(
        df,
        names="Churn",
        title="Churn Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )