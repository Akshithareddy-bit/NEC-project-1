import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

genders = ["Male", "Female"]
categories = ["Electronics", "Fashion", "Groceries", "Home", "Sports"]

budget_products = ["T-Shirt", "Groceries", "Household Products"]
medium_products = ["Watch", "Shoes", "Headphones"]
luxury_products = ["Smartphone", "Laptop", "Gaming Console"]

data = []

for i in range(n):

    age = np.random.randint(18, 65)

    gender = np.random.choice(genders)

    annual_budget = np.random.randint(10000, 100000)

    browsing_time = np.random.randint(5, 120)

    discount_sensitivity = np.random.randint(1, 10)

    purchase_frequency = np.random.randint(1, 20)

    last_purchase_days = np.random.randint(1, 365)

    satisfaction = np.random.randint(1, 10)

    loyalty = np.random.randint(1, 100)

    category = np.random.choice(categories)

    if annual_budget < 25000:

        segment = "Budget"

        product = np.random.choice(budget_products)

        purchase_amount = np.random.randint(500, 5000)

    elif annual_budget < 60000:

        segment = "Medium"

        product = np.random.choice(medium_products)

        purchase_amount = np.random.randint(5000, 25000)

    else:

        segment = "Luxury"

        product = np.random.choice(luxury_products)

        purchase_amount = np.random.randint(25000, 80000)

    churn = 1 if (
        loyalty < 30
        and satisfaction < 5
        and last_purchase_days > 150
    ) else 0

    data.append([
        i + 1,
        age,
        gender,
        annual_budget,
        category,
        browsing_time,
        discount_sensitivity,
        category,
        product,
        purchase_amount,
        segment,
        purchase_frequency,
        last_purchase_days,
        satisfaction,
        loyalty,
        churn
    ])

columns = [
    "Customer_ID",
    "Age",
    "Gender",
    "Annual_Budget",
    "Preferred_Category",
    "Browsing_Time",
    "Discount_Sensitivity",
    "Product_List_Viewed",
    "Purchased_Product",
    "Purchase_Amount",
    "Customer_Segment",
    "Purchase_Frequency",
    "Last_Purchase_Days",
    "Customer_Satisfaction",
    "Loyalty_Score",
    "Churn"
]

df = pd.DataFrame(data, columns=columns)

df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("data/customer_dataset.csv", index=False)

print("Dataset generated successfully")
print(df.head())