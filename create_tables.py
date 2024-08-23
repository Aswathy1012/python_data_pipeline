from dotenv import load_dotenv
import os
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Retrieve the connection details from environment variables
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# Establish a connection to PostgreSQL
connection = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

cursor = connection.cursor()

# Example: Create a table
# cursor.execute("""
# CREATE TABLE test_schema.my_table (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     age INTEGER,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """)

# Create a table products
cursor.execute("""
CREATE TABLE test_schema.products (
    Product_ID INTEGER  PRIMARY KEY,
    Product_Name VARCHAR(100),
    Category VARCHAR(100),
    Price REAL,
    Stock_Available INTEGER
);
""")
cursor.execute("""
CREATE TABLE test_schema.products_db_csv (
    product_id INTEGER  PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(100),
    price REAL,
    stock_available INTEGER
);
""")
#Create a table customer_data
cursor.execute("""
CREATE TABLE test_schema.customer_data (
    Customer_ID INTEGER PRIMARY KEY,
    Customer_Name VARCHAR(100),
    Age INTEGER,
    Gender VARCHAR(100),
    Location VARCHAR(100),
    Date_Joined TIMESTAMP
);
""")

# Create a table transactions
cursor.execute("""
CREATE TABLE test_schema.transactions (
    Transaction_ID INTEGER PRIMARY KEY,
    Customer_ID INTEGER REFERENCES test_schema.customer_data(Customer_ID),
    Product_ID INTEGER REFERENCES test_schema.products(Product_ID),
    Quantity INTEGER,
    Transaction_Date TIMESTAMP,
    Total_Amount REAL
);
""")

# Create a table sales_data
cursor.execute("""
CREATE TABLE test_schema.sales_data (
    Transaction_ID INTEGER  REFERENCES test_schema.transactions(Transaction_ID),
    Product_ID INTEGER REFERENCES test_schema.products(Product_ID),
    Quantity INTEGER,
    Price REAL,
    Transaction_Date TIMESTAMP
);
""")

# Create a table exchange_rates
cursor.execute("""
CREATE TABLE test_schema.exchange_rates (
    Currency_Code  VARCHAR(100),
    Exchange_Rate REAL,
    Date TIMESTAMP
);
""")

# Commit and close the connection
connection.commit()
cursor.close()
connection.close()
