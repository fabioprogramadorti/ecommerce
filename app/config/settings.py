import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    API_URL = os.getenv("API_URL")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
