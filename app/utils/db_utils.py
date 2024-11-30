import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """
    Create and return a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",         # Replace with your MySQL host
            user="your_username",     # Replace with your MySQL username
            password="your_password", # Replace with your MySQL password
            database="youtube_transcript"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise