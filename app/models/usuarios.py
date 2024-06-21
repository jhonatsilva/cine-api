from app import db

class User(db.Model):
    __tablename__ = 'usuarios_filmes'
    
    num_seq_usuario = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40), nullable=False)
    senha = db.Column(db.String(40), nullable=False)
   

    def json(self):
        return {
            'num_seq_usuario': self.num_seq_usuario,
            'login': self.login,
            'senha': self.senha
        }
