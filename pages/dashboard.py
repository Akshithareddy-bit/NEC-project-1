import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard():

    st.header("📊 Customer Intelligence Dashboard")

    df = pd.read_csv("data/customer_dataset.csv")

    total_customers = len(df)
    avg_budget = df["Annual_Budget"].mean()
    avg_purchase = df["Purchase_Amount"].mean()
    avg_loyalty = df["Loyalty_Score"].mean()

    churn_rate = df["Churn"].mean() * 100

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric("Customers", total_customers)
    c2.metric("Avg Budget", f"₹{avg_budget:,.0f}")
    c3.metric("Avg Purchase", f"₹{avg_purchase:,.0f}")
    c4.metric("Loyalty Score", f"{avg_loyalty:.1f}")
    c5.metric("Churn Rate", f"{churn_rate:.1f}%")

    st.divider()

    col1,col2 = st.columns(2)

    with col1:
        fig = px.pie(
            df,
            names="Customer_Segment",
            title="Customer Segments"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(
            df,
            x="Age",
            title="Age Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    col3,col4 = st.columns(2)

    with col3:
        fig = px.scatter(
            df,
            x="Annual_Budget",
            y="Purchase_Amount",
            color="Customer_Segment",
            title="Budget vs Purchase Amount"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        revenue = (
            df.groupby("Preferred_Category")["Purchase_Amount"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            revenue,
            x="Preferred_Category",
            y="Purchase_Amount",
            title="Revenue by Category"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Customer Dataset")

    st.dataframe(
        df.head(100),
        use_container_width=True
    )