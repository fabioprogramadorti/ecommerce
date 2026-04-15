import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    DB_HOST = os.getenv("DB_HOST", "db")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "orders")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    API_URL = os.getenv(
        "API_URL",
        "https://jsonplaceholder.typicode.com/posts"
    )

    RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()