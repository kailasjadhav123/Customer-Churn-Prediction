import mysql.connector
import numpy as np
import pandas as pd
from config import DB_CONFIG

np.random.seed(42)

# 1. Create a simple dataset /

n = 1000

df = pd.DataFrame({
    "customer_id": [f"C{i:04d}" for i in range(1, n + 1)],
    "age": np.random.randint(18, 61, n),
    "tenure": np.random.randint(1, 61, n),
    "monthly_spend": np.round(np.random.uniform(500, 10000, n), 2),
    "total_orders": np.random.randint(1, 51, n),
    "complaints": np.random.randint(0, 7, n),
    "last_purchase_days": np.random.randint(1, 121, n),
    "support_calls": np.random.randint(0, 11, n)
})


risk_score = (
    0.03 * df["complaints"]
    + 0.025 * df["support_calls"]
    + 0.006 * df["last_purchase_days"]
    - 0.015 * df["tenure"]
)

probability = 1 / (1 + np.exp(-risk_score))
df["churn"] = (np.random.random(n) < probability).astype(int)

# 2. Connect to MySQL/
connection = mysql.connector.connect(**DB_CONFIG)
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    age INT,
    tenure INT,
    monthly_spend DECIMAL(10,2),
    total_orders INT,
    complaints INT,
    last_purchase_days INT,
    support_calls INT,
    churn INT
)
""")

# Start fresh when rerunning the project //
cursor.execute("DELETE FROM customers")

insert_query = """
INSERT INTO customers
(customer_id, age, tenure, monthly_spend, total_orders,
 complaints, last_purchase_days, support_calls, churn)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

data = [tuple(row) for row in df.itertuples(index=False, name=None)]
cursor.executemany(insert_query, data)

connection.commit()

print(f"{len(data)} customers inserted into MySQL.")

cursor.close()
connection.close()
