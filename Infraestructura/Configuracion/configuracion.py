import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    db_host: str = os.getenv("DB_HOST")
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_port: int = os.getenv("DB_PORT")
    db_engine: str = os.getenv("DB_ENGINE")
    db_name: str = os.getenv("DB_NAME")

    class Config:
        env_file = str(env_path)

settings = Settings()

URL = f"{settings.db_engine}://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

print(settings.db_host)
print(settings.db_user)
print(settings.db_password)
print(settings.db_port)
print(settings.db_engine)
print(settings.db_name)
