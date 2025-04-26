# app/core/config.py

import os
from dotenv import load_dotenv

# Determine the environment (default to 'development')
ENV = os.getenv("ENV", "development")

# Load the appropriate .env file
if ENV == "development":
    load_dotenv(".env.development")
else:
    load_dotenv(".env")


class Settings:
    """
    Centralized settings for the application, including API keys and database configuration.
    """

    # General application settings
    ENV: str = ENV
    APP_NAME: str = os.getenv("APP_NAME", "YouTube Transcript API")
    VERSION: str = os.getenv("VERSION", "1.0.0")

    # OpenAI configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    print(OPENAI_API_KEY)

    # Database configuration
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "youtube_transcript")

    def get_database_url(self) -> str:
        """
        Constructs the database connection URL based on the environment variables.
        Returns:
            str: The database connection URL.
        """
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


# Create a settings instance to use throughout the application
settings = Settings()
