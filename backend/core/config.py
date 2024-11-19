import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(env_path)


class Setting:
    PROJECT_NAME: str = "Flight Booking Service🔥"
    PROJECT_VERSION: str = "1.0.0"

    BATABASE_URL = "sqlite:///./sql_app.db"
    FLIGHT_SERVICE_URL = os.getenv("FLIGHT_SERVICE_URL", "http://localhost:8000")

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

setting = Setting()
