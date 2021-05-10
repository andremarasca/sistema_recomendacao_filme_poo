from genero import Genero
from usuario import Usuario
from filme import Filme
from avaliacao import Avaliacao


class SistemaRecomendacaoUserBased:
    def __init__(self) -> None:
        self.usuarios = []
        self.filmes = []
        self.avaliacoes = []
        self.generos = []

    def importar_avaliacoes(self, dataset):
        pass
