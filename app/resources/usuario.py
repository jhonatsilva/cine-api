from flask_restful import Resource, reqparse
from app.models.usuarios import User
from app import db

class Usuarios(Resource):
    def get(self):
        usuarios = User.query.all()
        return {'Usuarios': [usuario.json() for usuario in usuarios]}

class UsuarioResource(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
    argumentos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank")

    def get(self, num_seq_usuario):
        usuario = User.query.filter_by(num_seq_usuario=num_seq_usuario).first()
        if usuario:
            return usuario.json()
        return {'message': 'User not found'}, 404

    def post(self, num_seq_usuario):
        if User.query.filter_by(num_seq_usuario=num_seq_usuario).first():
            return {'message': f"User with num_seq_usuario '{num_seq_usuario}' already exists."}, 400

        dados = UsuarioResource.argumentos.parse_args()
        usuario = User(num_seq_usuario=num_seq_usuario, **dados)
        db.session.add(usuario)
        db.session.commit()

        return usuario.json(), 201

    def put(self, num_seq_usuario):
        dados = UsuarioResource.argumentos.parse_args()
        usuario = User.query.filter_by(num_seq_usuario=num_seq_usuario).first()

        if usuario:
            usuario.login = dados['login']
            usuario.senha = dados['senha']
        else:
            usuario = User(num_seq_usuario=num_seq_usuario, **dados)
            db.session.add(usuario)
        
        db.session.commit()
        return usuario.json(), 200 if usuario else 201

    def delete(self, num_seq_usuario):
        usuario = User.query.filter_by(num_seq_usuario=num_seq_usuario).first()
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return {'message': 'User deleted!'}
        return {'message': 'User not found'}, 404
