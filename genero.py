
class Genero:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.filmes = {}

    def inserir_filme(self, filme):
        self.filmes[filme.movie_id] = filme
