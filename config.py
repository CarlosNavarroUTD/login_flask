from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno desde el archivo .env

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_HOST = os.environ.get('DB_HOST') 
    DB_USER = os.environ.get('DB_USER') 
    DB_PASSWORD = os.environ.get('DB_PASSWORD') 
    DB_NAME = os.environ.get('DB_NAME') 


    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

