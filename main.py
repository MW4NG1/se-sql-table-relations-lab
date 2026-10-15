# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("""
SELECT e.first_name, e.last_name, e.title 
FROM employees e
JOIN offices o ON e.office_id = o.id
WHERE o.city = 'Boston';
""", conn)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""
SELECT o.id, o.city 
FROM offices o
LEFT JOIN employees e ON o.id = e.office_id
GROUP BY o.id
HAVING COUNT(e.id) = 0;
""", conn)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""
SELECT e.first_name, e.last_name, o.city, o.state
FROM employees e
LEFT JOIN offices o ON e.office_id = o.id
ORDER BY e.first_name, e.last_name;
""", conn)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""
SELECT c.contact_first_name, c.contact_last_name, c.phone, c.sales_rep_employee_number
FROM customers c
LEFT JOIN orders o ON c.customer_number = o.customer_number
WHERE o.order_number IS NULL
ORDER BY c.contact_last_name;
""", conn)

# STEP 5
# Replace None with your code
df_payment = None

# STEP 6
# Replace None with your code
df_credit = None

# STEP 7
# Replace None with your code
df_product_sold = None

# STEP 8
# Replace None with your code
df_total_customers = None

# STEP 9
# Replace None with your code
df_customers = None

# STEP 10
# Replace None with your code
df_under_20 = None

conn.close()