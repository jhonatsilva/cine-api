class filmeModel:
    def __init__(self, num_seq_filme, nome, duracao, classificacao, genero):
        self.num_seq_filme = num_seq_filme
        self.nome = nome
        self.duracao = duracao
        self.classificacao = classificacao
        self.genero = genero

    def json(self):
        return {
            'num_seq_filme': self.num_seq_filme,
            'nome': self.nome,
            'duracao': self.duracao,
            'classificacao': self.classificacao,
            'genero': self.genero
        }