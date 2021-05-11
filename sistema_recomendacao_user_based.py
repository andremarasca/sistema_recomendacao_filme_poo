from genero import Genero
from occupation import Occupation
from usuario import Usuario
from filme import Filme
from avaliacao import Avaliacao
from read_dataset import read_dataset
import pandas as pd
from sistema_recomendacao import SistemaRecomendacao


class SistemaRecomendacaoUserBased(SistemaRecomendacao):
    def __init__(self, user_filename, genre_filename, item_filename, data_filename) -> None:
        super().__init__(user_filename, genre_filename, item_filename, data_filename)

    def select_target_instances(self, target_movie_id):

        # self.filmes[target_movie_id] o obj filme de target_movie_id
        # self.filmes[target_movie_id].avaliacoes é um dict e a chave é o user_id
        target_users = self.filmes[target_movie_id].avaliacoes.keys()

        # o primeiro indice do pandas são as colunas, pode-se passar uma lista para filtrar
        return self.rating_matrix[target_users]

    def select_user_target(self, target_user_id):
        return self.rating_matrix[target_user_id]
