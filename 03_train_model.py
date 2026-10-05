import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

from config import DB_CONFIG

# 1. Read data from MySQL /
connection = mysql.connector.connect(**DB_CONFIG)

query = "SELECT * FROM customers"
df = pd.read_sql(query, connection)

connection.close()

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nChurn count:")
print(df["churn"].value_counts())

# 2. Basic analysis /
print("\nAverage values by churn:")
print(
    df.groupby("churn")[
        ["tenure", "monthly_spend", "total_orders", "complaints",
         "last_purchase_days", "support_calls"]
    ].mean().round(2)
)

# 3. Prepare data for ML /
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
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 4. Train Logistic Regression /
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# 5. Evaluate the model /
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\nMODEL RESULTS")
print(f"Accuracy : {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall   : {recall:.2%}")
print(f"F1 Score : {f1:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# 6. Predict churn for all customers /
df["predicted_churn"] = model.predict(X)
df["churn_probability"] = model.predict_proba(X)[:, 1]

df.to_csv("outputs/customer_churn_predictions.csv", index=False)

# 7. Create simple charts /
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("outputs/churn_distribution.png")
plt.close()

plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="churn", y="last_purchase_days")
plt.title("Churn vs Days Since Last Purchase")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Days Since Last Purchase")
plt.tight_layout()
plt.savefig("outputs/churn_vs_last_purchase.png")
plt.close()

print("\nPrediction file and charts were saved in the outputs folder.")
