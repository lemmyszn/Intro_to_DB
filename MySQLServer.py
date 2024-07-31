import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing the connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',          # Replace with your MySQL server host
            user='root',      # Replace with your MySQL username
            password='#44bulldogs'   # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Connected to MySQL server successfully!")

            cursor = connection.cursor()

            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
