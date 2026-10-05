import mysql.connector
from config import DB_CONFIG

# Connect without selecting a database.
connection = mysql.connector.connect(
    host=DB_CONFIG["host"],
    port=DB_CONFIG["port"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"]
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS customer_churn_db")
print("Database customer_churn_db is ready.")

cursor.close()
connection.close()
