"""
Author: Jhonathan Silva
Version 1.0.0
Date: 2024-06-20
"""
from app import create_app
from flask_restful import Api
from app.resources.filme import Filmes, FilmeResource
from app.resources.usuario import Usuarios, UsuarioResource

app = create_app()

# Inicializar a API Flask-RESTful
api = Api(app)

# Adicionar os recursos da API
api.add_resource(Filmes, '/filmes')
api.add_resource(FilmeResource, '/filmes/<int:num_seq_filme>')
api.add_resource(Usuarios, '/usuarios')
api.add_resource(UsuarioResource, '/usuarios/<int:num_seq_usuario>')
# Rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)
