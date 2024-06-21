from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://jhonathan:admin@127.0.0.1:3306/cinematicadb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
