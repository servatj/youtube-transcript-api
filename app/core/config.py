# app/core/config.py

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Settings:
    """
    Settings for the application, such as API keys and other environment-specific variables.
    """
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    APP_NAME: str = "YouTube Transcript API"
    VERSION: str = "1.0.0"

# Create a settings instance to use throughout the application
settings = Settings()