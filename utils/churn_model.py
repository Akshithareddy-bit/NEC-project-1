import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("data/customer_dataset.csv")

X = df[
    [
        "Purchase_Frequency",
        "Last_Purchase_Days",
        "Customer_Satisfaction",
        "Loyalty_Score"
    ]
]

y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

preds = model.predict(X_test)

accuracy = accuracy_score(y_test, preds)

print(f"Churn Model Accuracy: {accuracy:.2f}")

joblib.dump(
    model,
    "models/churn_model.pkl"
)

print("Churn model saved successfully")