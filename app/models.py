from app import db

class Filme(db.Model):
    __tablename__ = 'catalogo_filmes'
    
    num_seq_filme = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    duracao = db.Column(db.String(20), nullable=False)
    classificacao = db.Column(db.String(20), nullable=False)
    genero = db.Column(db.String(50), nullable=False)

    def json(self):
        return {
            'num_seq_filme': self.num_seq_filme,
            'nome': self.nome,
            'duracao': self.duracao,
            'classificacao': self.classificacao,
            'genero': self.genero
        }
