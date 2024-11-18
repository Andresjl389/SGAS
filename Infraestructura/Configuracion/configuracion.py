import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

# Cargar el archivo .env
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Configuración de Pydantic Settings
class Settings(BaseSettings):
    db_host: str
    db_user: str
    db_password: str
    db_engine: str
    db_name: str
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_expiration_time: int

    class Config:
        env_file = str(env_path)

# Instancia de configuración
settings = Settings()

# Configuración de la base de datos
URL = f"{settings.db_engine}://{settings.db_user}:{settings.db_password}@{settings.db_host}/{settings.db_name}"
engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Imprimir valores para depuración
print("Base de Datos:", settings.db_host)
print("Usuario:", settings.db_user)
print("Clave JWT:", settings.jwt_secret_key)
print("Algoritmo JWT:", settings.jwt_algorithm)
print("Expiración JWT:", settings.jwt_expiration_time)
