from numpy.core.records import array
from metricas_similaridade import DistanciaCosseno
from avaliacao import Avaliacao
import numpy as np
from estatistica import Estatistica


class Usuario(Estatistica):
    def __init__(self, user_id: str, age: int, gender: str, occupation, zip_code: str) -> None:
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.zip_code = zip_code
        self.avaliacoes = {}

    def inserir_avaliacao(self, avaliacao):
        self.avaliacoes[avaliacao.filme.movie_id] = avaliacao

    def rating_medio(self):
        soma = 0
        qtd = 0
        for movie_id in self.avaliacoes:
            soma += self.avaliacoes[movie_id].rating
            qtd += 1
        return soma / qtd

    def classificar_filme(self, filme, nota: float):
        pass

    def recupera_classificacao(self) -> float:
        return 0

    def calcula_similaridade(self, outro_usuario) -> float:
        # return DistanciaCosseno.calcula_distancia(self, outro_usuario)
        return 0

    def as_array(self):
        list_rating = []
        avaliacoes: dict = self.avaliacoes
        for movie_id in avaliacoes:
            avaliacao: Avaliacao = avaliacoes[movie_id]
            list_rating.append(avaliacao.rating)
        return np.array(list_rating)
