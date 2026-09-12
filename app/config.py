"""Application configuration loaded from environment variables."""

import os


class Settings:
    """Minimal settings for the POC."""

    app_name: str = os.getenv("APP_NAME", "PDF RAG Chatbot")
    app_environment: str = os.getenv("APP_ENVIRONMENT", "development")


settings = Settings()
