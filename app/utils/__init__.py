"""
This module initializes the utils package and provides utility functions for the application.
"""

from app.db_utils import get_db_connection

__all__ = ["get_db_connection"]