# Customer Churn Prediction using Python, SQL & Machine Learning

## Project Objective
Predict whether a customer is likely to churn using customer behavior data.

## Technologies
- Python
- Pandas
- NumPy
- SQL / MySQL
- Scikit-learn
- Matplotlib
- Seaborn
- Power BI (optional)
- Git/GitHub

## Project Flow
MySQL -> Python -> Data Cleaning -> EDA -> Feature Engineering -> Machine Learning -> Prediction -> Dashboard

## Database
Database name: `customer_churn_db`

Table: `customers`

Columns:
- customer_id
- age
- tenure
- monthly_spend
- total_orders
- complaints
- last_purchase_days
- support_calls
- churn

## How to Run

### 1. Install MySQL
Make sure MySQL Server is installed and running.

### 2. Create Python environment
```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

### 3. Install packages
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL
Copy `.env.example` to `.env` and put your MySQL password in `.env`.

Example:
```text
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=customer_churn_db
```

### 5. Create database
Run:
```bash
python 01_create_database.py
```

### 6. Generate and insert data
Run:
```bash
python 02_generate_and_insert_data.py
```

This creates 1,000 customers and inserts them into MySQL.

### 7. Train the ML model
Run:
```bash
python 03_train_model.py
```

This:
- Reads data from MySQL
- Checks missing values
- Performs basic analysis
- Trains Logistic Regression
- Calculates accuracy, precision, recall and F1-score
- Creates predictions
- Saves CSV and charts in `outputs`

### 8. Test a new customer
Run:
```bash
python 04_predict_new_customer.py
```
Name: Kailas Jadhav
Email: kailasjadhav8010@gmail.com
Number: 8010061035
