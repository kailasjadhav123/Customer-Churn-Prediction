CREATE DATABASE customer_churn_db;
USE customer_churn_db;

CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    age INT,
    tenure INT,
    monthly_spend DECIMAL(10,2),
    total_orders INT,
    complaints INT,
    last_purchase_days INT,
    support_calls INT,
    churn INT
);
