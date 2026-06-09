import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from pages.segmentation import show_segmentation

from utils.recommendation_engine import (
    recommend_products,
    match_score
)

# -------------------
# PAGE CONFIG
# -------------------

st.set_page_config(
    page_title="AI Customer Intelligence",
    page_icon="📊",
    layout="wide"
)

# -------------------
# CSS
# -------------------

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -------------------
# LOAD DATA
# -------------------

df = pd.read_csv(
    "data/customer_dataset.csv"
)

# -------------------
# TITLE
# -------------------

st.title(
    "🤖 AI Driven Customer Intelligence Platform"
)

st.markdown("---")

# -------------------
# TABS
# -------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Dashboard",
        "Prediction",
        "Segmentation",
        "Churn Analysis",
        "Recommendations"
    ]
)

# ====================================================
# TAB 1 DASHBOARD
# ====================================================

with tab1:

    st.header("📊 Dashboard Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Customers", len(df))
    c2.metric("Avg Budget", f"₹{int(df['Annual_Budget'].mean()):,}")
    c3.metric("Total Revenue", f"₹{int(df['Purchase_Amount'].sum()):,}")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        fig1 = px.pie(
            df,
            names="Customer_Segment",
            title="Customer Segment Distribution"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:

        fig2 = px.bar(
            df.groupby("Customer_Segment")["Purchase_Amount"]
            .sum()
            .reset_index(),
            x="Customer_Segment",
            y="Purchase_Amount",
            title="Revenue by Segment"
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    st.subheader("🛍️ Preferred Category Distribution")

    fig3 = px.pie(
        df,
        names="Preferred_Category",
        title="Preferred Category Distribution"
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("🏆 Top Purchased Products")

    top_products = (
        df["Purchased_Product"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_products.columns = ["Product", "Count"]

    fig4 = px.bar(
        top_products,
        x="Product",
        y="Count",
        title="Top Purchased Products"
    )
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("💰 Annual Budget Distribution")

    fig5 = px.histogram(
        df,
        x="Annual_Budget",
        nbins=20,
        title="Annual Budget Distribution"
    )
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("📈 Purchase Amount Distribution")

    fig6 = px.histogram(
        df,
        x="Purchase_Amount",
        nbins=20,
        title="Purchase Amount Distribution"
    )
    st.plotly_chart(fig6, use_container_width=True)

    st.markdown("---")

    st.subheader("📥 Download Dataset")

    st.download_button(
    label="⬇️ Download Full Dataset",
    data=df.to_csv(index=False),
    file_name="customer_dataset.csv",
    mime="text/csv",
    key="download_tab1"
)

    

# ====================================================
# TAB 2 PREDICTION
# ====================================================

with tab2:

    st.header("🤖 Customer Segment Prediction")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            18,
            80,
            25
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        budget = st.number_input(
            "Annual Budget",
            10000,
            100000,
            30000
        )

    with col2:

        browsing = st.slider(
            "Browsing Time",
            1,
            120,
            20
        )

        discount = st.slider(
            "Discount Sensitivity",
            1,
            10,
            5
        )

    if st.button("Predict Customer Segment"):

        model = joblib.load(
            "models/model.pkl"
        )

        encoder = joblib.load(
            "models/segment_encoder.pkl"
        )

        gender_value = 1 if gender == "Male" else 0

        input_data = pd.DataFrame(
            [[
                age,
                gender_value,
                budget,
                browsing,
                discount
            ]],
            columns=[
                "Age",
                "Gender",
                "Annual_Budget",
                "Browsing_Time",
                "Discount_Sensitivity"
            ]
        )

        prediction = model.predict(
            input_data
        )[0]

        probabilities = model.predict_proba(
            input_data
        )[0]

        confidence = max(
            probabilities
        ) * 100

        segment = encoder.inverse_transform(
            [prediction]
        )[0]

        st.success(
            f"🎯 Predicted Segment: {segment}"
        )

        st.info(
            f"📊 Confidence Score: {confidence:.2f}%"
        )

        if confidence > 85:

            st.success(
                "High Confidence Prediction ✅"
            )

        elif confidence > 60:

            st.warning(
                "Medium Confidence Prediction ⚠️"
            )

        else:

            st.error(
                "Low Confidence Prediction ❌"
            )

    st.markdown("---")

    st.subheader("📊 Customer Segment Distribution")

    segment_counts = (
        df["Customer_Segment"]
        .value_counts()
        .reset_index()
    )

    segment_counts.columns = [
        "Segment",
        "Count"
    ]

    fig = px.pie(
        segment_counts,
        names="Segment",
        values="Count",
        title="Customer Segment Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("📈 Segment Statistics")

    segment_stats = (
        df.groupby("Customer_Segment")
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

    st.dataframe(
        segment_stats,
        use_container_width=True
    )

    st.subheader("📥 Download Dataset")

    csv = df.to_csv(index=False)

    st.download_button(
    label="Download Dataset",
    data=csv,
    file_name="customer_dataset.csv",
    mime="text/csv",
    key="download_tab2"
)

# ====================================================
# TAB 3 SEGMENTATION
# ====================================================

with tab3:
    show_segmentation()

# ====================================================
# TAB 4 CHURN
# ====================================================

# ====================================================
# TAB 4 CHURN ANALYSIS
# ====================================================

with tab4:

    st.header("📉 Customer Churn Analysis")

    churned = len(df[df["Churn"] == 1])

    churn_rate = round(df["Churn"].mean() * 100, 2)
    retention_rate = round((1 - df["Churn"].mean()) * 100, 2)
    avg_loyalty = round(df["Loyalty_Score"].mean(), 2)

    c1, c2, c3 = st.columns(3)

    c1.metric("Churn Customers", churned)
    c2.metric("Churn Rate", f"{churn_rate}%")
    c3.metric("Retention Rate", f"{retention_rate}%")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(df, names="Churn", title="Churn Distribution")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(
            df,
            x="Loyalty_Score",
            color="Churn",
            title="Loyalty Score Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("📋 Churn Customers Table")

    churn_df = df[df["Churn"] == 1]
    st.dataframe(churn_df, use_container_width=True)

    st.download_button(
        "Download Churn Dataset",
        churn_df.to_csv(index=False),
        "churn_customers.csv",
        "text/csv"
    )

    st.markdown("---")

    # ---------------- CHURN PREDICTION ----------------

    st.header("🔮 Churn Prediction")

    purchase_freq = st.slider("Purchase Frequency", 1, 20, 5)
    last_purchase = st.slider("Last Purchase Days", 1, 365, 30)
    satisfaction = st.slider("Customer Satisfaction", 1, 10, 5)
    loyalty = st.slider("Loyalty Score", 0, 100, 50)

    if st.button("Predict Churn"):

        churn_model = joblib.load("models/churn_model.pkl")

        input_data = pd.DataFrame([[
            purchase_freq,
            last_purchase,
            satisfaction,
            loyalty
        ]], columns=[
            "Purchase_Frequency",
            "Last_Purchase_Days",
            "Customer_Satisfaction",
            "Loyalty_Score"
        ])

        prediction = churn_model.predict(input_data)[0]
        probability = churn_model.predict_proba(input_data)[0][1]

        if prediction == 1:
            st.error("⚠️ Customer Likely To Churn")
        else:
            st.success("✅ Customer Likely To Stay")

        st.info(f"Churn Probability: {probability*100:.2f}%")

    st.markdown("---")

    st.download_button(
    "Download Full Dataset",
    df.to_csv(index=False),
    "customer_dataset.csv",
    "text/csv",
    key="download_tab4"
)
    
# ====================================================
# TAB 5 RECOMMENDATION
# ====================================================

with tab5:

    st.header("🛍️ Smart Recommendation Engine")

    budget = st.number_input(
        "Enter Customer Budget",
        1000,
        100000,
        25000
    )

    if st.button("Generate Recommendations"):

        products = recommend_products(budget)
        score = match_score(budget)

        st.success(f"Match Score: {score}%")

        st.subheader("🛒 Recommended Products")

        for p in products:
            st.write("✔️", p)

        # --- extra insight
        if budget > 60000:
            segment = "Luxury Customer"
        elif budget > 25000:
            segment = "Mid Range Customer"
        else:
            segment = "Budget Customer"

        st.info(f"Detected Segment: {segment}")

    st.markdown("---")

    st.subheader("📊 Quick Insights")

    col1, col2, col3 = st.columns(3)

    col1.metric("High Value Range", "60K+")
    col2.metric("Mid Range", "25K - 60K")
    col3.metric("Budget Range", "<25K")

    st.markdown("---")

    st.subheader("📥 Download Dataset")

    csv = df.to_csv(index=False)

    st.download_button(
    label="⬇️ Download Full Dataset",
    data=df.to_csv(index=False),
    file_name="customer_dataset.csv",
    mime="text/csv",
    key="download_tab5"
)