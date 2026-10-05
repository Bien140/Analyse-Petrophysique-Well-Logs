import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

def get_engine():
    # Crée et retourne le moteur de connexion à PostgreSQL.
    load_dotenv()
    
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    
    DATABASE_URL = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    return create_engine(DATABASE_URL)