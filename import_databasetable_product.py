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

# Copy data from products_db_csv to the target table products with different column names
copy_query = """
    INSERT INTO test_schema.products (Product_ID, Product_Name, Category, Price, Stock_Available)
    SELECT product_id, product_name, category, price, stock_available
    FROM test_schema.products_db_csv;
"""

try:
    cursor.execute(copy_query)
    connection.commit()
    print("Data copied successfully")
except Exception as e:
    print(f"Error: {e}")
    connection.rollback()
finally:
    cursor.close()
    connection.close()
