from flask_restful import Resource, reqparse
from models.filme import filmeModel

filmes = [
    {
        'num_seq_filme': '1',
        'nome': 'Batman',
        'duracao': '2h30min',
        'classificacao': 'Livre',
        'genero': 'Ação'
    },
    {
        'num_seq_filme': '2',
        'nome': 'Super Man',
        'duracao': '2h30min',
        'classificacao': 'Livre',
        'genero': 'Ação'
    },
    {
        'num_seq_filme': '3',
        'nome': 'Mulher Maravilha 1984',
        'duracao': '2h30min',
        'classificacao': 'Livre',
        'genero': 'Ação'
    }
]

class Filmes(Resource):
    def get(self):
        return {'Filmes': filmes}

class Filme(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('duracao')
    argumentos.add_argument('classificacao')
    argumentos.add_argument('genero')

    @staticmethod
    def find_filme(num_seq_filme):
        for filme in filmes:
            if filme['num_seq_filme'] == num_seq_filme:
                return filme
        return None

    def get(self, num_seq_filme):
        filme = Filme.find_filme(num_seq_filme)
        if filme:
            return filme
        return {'message': 'Filme not found'}, 404

    def post(self, num_seq_filme):
        dados = Filme.argumentos.parse_args()
        filme_objeto = filmeModel(num_seq_filme, **dados)
        novo_filme = filme_objeto.json()

        filmes.append(novo_filme)
        return novo_filme, 200

    def put(self, num_seq_filme):
        dados = Filme.argumentos.parse_args()
        filme_objeto = filmeModel(num_seq_filme, **dados)
        novo_filme = filme_objeto.json()

        filme = Filme.find_filme(num_seq_filme)
        if filme:
            filme.update(novo_filme)
            return novo_filme, 200 # ok
        filmes.append(novo_filme)
        return novo_filme, 201 # created

    def delete(self, num_seq_filme):
        global filmes # para pegar os valores da variavel chamada abaixo, variavel ja foi criada la em cima
        filmes = [filme for filme in filmes if filme['num_seq_filme'] != num_seq_filme] 
        return {'message': 'Filme excluído!'}
