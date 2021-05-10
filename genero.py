
class Genero:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.filmes = []

    def inserir_filmes(self, filme):
        self.filmes.append(filme)
