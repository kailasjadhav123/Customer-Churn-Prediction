import mysql.connector
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from config import DB_CONFIG

# Read data from MySQL /
connection = mysql.connector.connect(**DB_CONFIG)
df = pd.read_sql("SELECT * FROM customers", connection)
connection.close()

features = [
    "age",
    "tenure",
    "monthly_spend",
    "total_orders",
    "complaints",
    "last_purchase_days",
    "support_calls"
]

X = df[features]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Example /
new_customer = pd.DataFrame([{
    "age": 30,
    "tenure": 4,
    "monthly_spend": 1500,
    "total_orders": 5,
    "complaints": 4,
    "last_purchase_days": 90,
    "support_calls": 6
}])

prediction = model.predict(new_customer)[0]
probability = model.predict_proba(new_customer)[0][1]

print("\nNEW CUSTOMER PREDICTION")
print("Churn prediction:", "Likely to Churn" if prediction == 1 else "Likely to Stay")
print(f"Churn probability: {probability:.2%}")
