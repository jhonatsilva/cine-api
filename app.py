from flask import Flask
from flask_restful import  Api
from resources.filme import Filmes, Filme

app = Flask(__name__)
api = Api(app)
    
api.add_resource(Filmes, '/filmes')
api.add_resource(Filme, '/filmes/<string:num_seq_filme>')

if __name__== '__main__':
    app.run(debug=True)