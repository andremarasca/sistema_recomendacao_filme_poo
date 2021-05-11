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

    def select_target_instances(self, target_user_id):
        """ Construir lista de filmes que o usuário alvo já assistiu """
        user: Usuario = self.usuarios[target_user_id]
        target_movies = list(user.avaliacoes.keys())
        target_matrix = self.rating_matrix.loc[target_movies, :]
        return target_matrix

    def select_movie_target(self, target_movie_id):
        return self.rating_matrix.loc[target_movie_id, :]

# %% Coisa antiga apagar depois de terminar

    def select_user_target(self, target_user_id):
        return self.rating_matrix[target_user_id]

    def knn(self, n_neighbors, target_movie_id, target_user_id):

        target_matrix = self.select_target_instances(target_user_id)
        target_movie = self.select_movie_target(target_movie_id).tolist()

        list_similaridade = []

        for movie_id, curr_movie in target_matrix.iterrows():
            curr_movie = curr_movie.tolist()
            similaridade = ms.calcula_distancia(target_movie, curr_movie)
            list_similaridade.append((similaridade, movie_id))

        list_similaridade.sort(reverse=True)

        return list_similaridade[0:n_neighbors]

    def estimate_target_rating(self, n_neighbors, target_movie_id, target_user_id):
        # Estimar rating do filme alvo com média ponderada

        knn = self.knn(n_neighbors, target_movie_id, target_user_id)

        filmes = self.filmes

        soma = 0
        soma_peso = 0

        for i in knn:
            similaridade = i[0]
            movie_id = i[1]
            movie: Filme = filmes[movie_id]
            rating = movie.avaliacoes[target_user_id].rating

            soma += similaridade*rating
            soma_peso += similaridade

        target_rating = soma / soma_peso

        return target_rating
