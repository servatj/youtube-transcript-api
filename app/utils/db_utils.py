import psycopg2
from psycopg2 import OperationalError
from app.core.config import settings  # Import the settings instance


def get_db_connection():
    """
    Create and return a connection to the PostgreSQL database using settings from config.py.
    """
    try:
        connection = psycopg2.connect(
            host=settings.DB_HOST,  # Get host from settings
            user=settings.DB_USER,  # Get username from settings
            password=settings.DB_PASSWORD,  # Get password from settings
            dbname=settings.DB_NAME,  # Get database name from settings
            port=settings.DB_PORT,  # Get port from settings
        )
        return connection
    except OperationalError as e:
        print(f"Error connecting to PostgreSQL: {e}")
        raise
