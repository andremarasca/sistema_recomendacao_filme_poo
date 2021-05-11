from genero import Genero
from occupation import Occupation
from usuario import Usuario
from filme import Filme
from avaliacao import Avaliacao
from read_dataset import read_dataset
import pandas as pd
from sistema_recomendacao import SistemaRecomendacao
from metricas_similaridade import DistanciaCosseno as ms


class SistemaRecomendacaoItemBased(SistemaRecomendacao):
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

    def knn(self, n_neighbors, target_movie_id, target_user_id):

        target_matrix = self.select_target_instances(target_movie_id)
        target_user = self.select_user_target(target_user_id).tolist()

        list_similaridade = []

        for user_id in target_matrix:
            curr_user = target_matrix[user_id].tolist()
            similaridade = ms.calcula_distancia(target_user, curr_user)
            list_similaridade.append((similaridade, user_id))

        list_similaridade.sort(reverse=True)

        return list_similaridade[0:n_neighbors]

    def estimate_target_rating(self, n_neighbors, target_movie_id, target_user_id):
        # Estimar rating do filme alvo com média ponderada

        knn = self.knn(n_neighbors, target_movie_id, target_user_id)

        usuarios = self.usuarios

        soma = 0
        soma_peso = 0

        for i in knn:
            similaridade = i[0]
            user_id = i[1]
            user: Usuario = usuarios[user_id]
            rating = user.avaliacoes[target_movie_id].rating

            soma += similaridade*rating
            soma_peso += similaridade

        target_rating = soma / soma_peso

        return target_rating
