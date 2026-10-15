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
df_payment = pd.read_sql("""
SELECT c.contact_first_name, c.contact_last_name, p.amount, p.payment_date
FROM customers c
JOIN payments p ON c.customer_number = p.customer_number
ORDER BY CAST(p.amount AS REAL) DESC;
""", conn)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql("""
SELECT e.employee_number, e.first_name, e.last_name, COUNT(c.customer_number) AS customer_count
FROM employees e
JOIN customers c ON e.employee_number = c.sales_rep_employee_number
GROUP BY e.employee_number, e.first_name, e.last_name
HAVING AVG(c.credit_limit) > 90000
ORDER BY customer_count DESC;
""", conn)


# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""
SELECT p.product_name, COUNT(od.order_number) AS numorders, SUM(od.quantity_ordered) AS totalunits
FROM products p
JOIN orderdetails od ON p.product_code = od.product_code
GROUP BY p.product_code, p.product_name
ORDER BY totalunits DESC;
""", conn)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql("""
SELECT p.product_name, p.product_code, COUNT(DISTINCT o.customer_number) AS numpurchasers
FROM products p
JOIN orderdetails od ON p.product_code = od.product_code
JOIN orders o ON od.order_number = o.order_number
GROUP BY p.product_code, p.product_name
ORDER BY numpurchasers DESC;
""", conn)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql("""
SELECT COUNT(c.customer_number) AS n_customers, o.id AS office_code, o.city
FROM offices o
JOIN employees e ON o.id = e.office_id
JOIN customers c ON e.employee_number = c.sales_rep_employee_number
GROUP BY o.id, o.city
ORDER BY n_customers DESC;
""", conn)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql("""
SELECT DISTINCT e.employee_number, e.first_name, e.last_name, off.city, off.id AS office_code
FROM employees e
JOIN offices off ON e.office_id = off.id
JOIN customers c ON e.employee_number = c.sales_rep_employee_number
JOIN orders o ON c.customer_number = o.customer_number
JOIN orderdetails od ON o.order_number = od.order_number
WHERE od.product_code IN (
    SELECT p.product_code
    FROM products p
    JOIN orderdetails od_sub ON p.product_code = od_sub.product_code
    JOIN orders o_sub ON od_sub.order_number = o_sub.order_number
    GROUP BY p.product_code
    HAVING COUNT(DISTINCT o_sub.customer_number) < 20
);
""", conn)

conn.close()