from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializar a extensão SQLAlchemy
db = SQLAlchemy()

def create_app(config_class='config.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar a aplicação com SQLAlchemy
    db.init_app(app)

    # Importar os modelos para que sejam reconhecidos pelo SQLAlchemy
    from app.models import Filme

    # Criação do banco de dados
    with app.app_context():
        db.create_all()

    return app
