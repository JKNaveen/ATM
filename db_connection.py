import mysql.connector
from mysql.connector import Error

def create_table():
    connection = create_connection("localhost", "your_username", "your_password", "banking_system")
    create_accounts_table = """
    CREATE TABLE IF NOT EXISTS accounts (
      account_number VARCHAR(20) PRIMARY KEY,
      balance FLOAT NOT NULL,
      pin INT NOT NULL,
      account_type VARCHAR(20) NOT NULL,
      interest_rate FLOAT DEFAULT 0,
      overdraft_limit FLOAT DEFAULT 0
    );
    """
    execute_query(connection, create_accounts_table)

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Root@123",
            database="banking_accounts"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, params=()):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
