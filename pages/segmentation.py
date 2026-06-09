import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

def show_segmentation():

    st.header("🎯 Customer Segmentation")

    df = pd.read_csv("data/customer_dataset.csv")

    features = df[
        [
            "Annual_Budget",
            "Purchase_Amount",
            "Loyalty_Score"
        ]
    ]

    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    df["Cluster"] = kmeans.fit_predict(features)

    st.subheader("Customer Clusters")

    fig = px.scatter(
        df,
        x="Annual_Budget",
        y="Purchase_Amount",
        color=df["Cluster"].astype(str),
        size="Loyalty_Score",
        hover_data=["Age"],
        title="Customer Segmentation"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Cluster Distribution")

    pie = px.pie(
        df,
        names="Cluster",
        title="Cluster Share"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

    cluster_summary = (
        df.groupby("Cluster")
        [
            [
                "Annual_Budget",
                "Purchase_Amount",
                "Loyalty_Score"
            ]
        ]
        .mean()
        .round(2)
    )

    st.subheader("Cluster Summary")

    st.dataframe(
        cluster_summary,
        use_container_width=True
    )

    st.subheader("💰 Revenue Contribution by Cluster")

    revenue_cluster = (
        df.groupby("Cluster")["Purchase_Amount"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        revenue_cluster,
        x="Cluster",
        y="Purchase_Amount",
        text="Purchase_Amount",
        title="Revenue Contribution by Cluster"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("📥 Download Dataset")

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Dataset",
        data=csv,
        file_name="customer_segmentation.csv",
        mime="text/csv"
    )