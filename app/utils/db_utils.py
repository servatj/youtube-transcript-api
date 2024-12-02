import mysql.connector
from mysql.connector import Error
from app.core.config import settings  # Import the settings instance


def get_db_connection():
    """
    Create and return a connection to the MySQL database using settings from config.py.
    """
    try:
        connection = mysql.connector.connect(
            host=settings.DB_HOST,  # Get host from settings
            user=settings.DB_USER,  # Get username from settings
            password=settings.DB_PASSWORD,  # Get password from settings
            database=settings.DB_NAME,  # Get database name from settings
            port=settings.DB_PORT,  # Get port from settings
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise
