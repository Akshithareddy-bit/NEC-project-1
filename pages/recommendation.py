import streamlit as st

def show_recommendation():

    st.header(
        "Product Recommendation Engine"
    )

    budget = st.number_input(
        "Customer Budget",
        1000,
        100000
    )

    if st.button(
        "Recommend Products"
    ):

        if budget > 60000:

            products = [
                "Laptop",
                "Smartphone",
                "Gaming Console"
            ]

        elif budget > 25000:

            products = [
                "Watch",
                "Shoes",
                "Headphones"
            ]

        else:

            products = [
                "T-Shirt",
                "Groceries",
                "Home Products"
            ]

        st.success(
            "Recommended Products"
        )

        for p in products:
            st.write("✅", p)