from flask_restful import Resource, reqparse
from app.models.filmes import Filme
from app import db

class Filmes(Resource):
    def get(self):
        filmes = Filme.query.all()
        return {'Filmes': [filme.json() for filme in filmes]}

class FilmeResource(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank")
    argumentos.add_argument('duracao', type=str, required=True, help="The field 'duracao' cannot be left blank")
    argumentos.add_argument('classificacao', type=str, required=True, help="The field 'classificacao' cannot be left blank")
    argumentos.add_argument('genero', type=str, required=True, help="The field 'genero' cannot be left blank")

    def get(self, num_seq_filme):
        filme = Filme.query.filter_by(num_seq_filme=num_seq_filme).first()
        if filme:
            return filme.json()
        return {'message': 'Filme not found'}, 404

    def post(self, num_seq_filme):
        if Filme.query.filter_by(num_seq_filme=num_seq_filme).first():
            return {'message': f"Filme with num_seq_filme '{num_seq_filme}' already exists."}, 400

        dados = FilmeResource.argumentos.parse_args()
        filme = Filme(num_seq_filme=num_seq_filme, **dados)
        db.session.add(filme)
        db.session.commit()

        return filme.json(), 201

    def put(self, num_seq_filme):
        dados = FilmeResource.argumentos.parse_args()
        filme = Filme.query.filter_by(num_seq_filme=num_seq_filme).first()

        if filme:
            filme.nome = dados['nome']
            filme.duracao = dados['duracao']
            filme.classificacao = dados['classificacao']
            filme.genero = dados['genero']
        else:
            filme = Filme(num_seq_filme=num_seq_filme, **dados)
            db.session.add(filme)
        
        db.session.commit()
        return filme.json(), 200 if filme else 201

    def delete(self, num_seq_filme):
        filme = Filme.query.filter_by(num_seq_filme=num_seq_filme).first()
        if filme:
            db.session.delete(filme)
            db.session.commit()
            return {'message': 'Filme excluído!'}
        return {'message': 'Filme not found'}, 404
