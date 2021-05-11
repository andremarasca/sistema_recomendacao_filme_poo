from sistema_recomendacao_user_based import SistemaRecomendacaoUserBased
from sistema_recomendacao_item_based import SistemaRecomendacaoItemBased
from genero import Genero
from occupation import Occupation
from usuario import Usuario
from filme import Filme
from avaliacao import Avaliacao
from read_dataset import read_dataset
import pandas as pd
from metricas_similaridade import DistanciaCosseno as ms

srib = SistemaRecomendacaoItemBased(
    "ml-100k/u.user", "ml-100k/u.genre", "ml-100k/u.item", "ml-100k/u.data")

# %% Estimar o rating que o usuario alvo daria para o filme alvo se ele assistisse esse filme

srub = SistemaRecomendacaoUserBased(
    "ml-100k/u.user", "ml-100k/u.genre", "ml-100k/u.item", "ml-100k/u.data")

rating = srub.estimate_target_rating(
    n_neighbors=3, target_movie_id="1", target_user_id="3")

print(rating)

# %% Testes de acesso

# # Acessar a primeira avaliação a lista do usuário 100, mostrar o movie_id e o rating

# user_id = "100"
# user = srub.usuarios[user_id]
# aval = user.avaliacoes[0]
# rating = aval.rating
# movie_id = aval.filme.movie_id

# print(f"Usuario {user_id} avaliou o filme {movie_id} com nota {rating}")

# # Descobrir os generos do filme 123

# movie_id = "123"
# movie = srub.filmes[movie_id]
# generos = movie.generos
# for genero in generos:
#     print(f"Filme {movie_id} tem genero {genero.nome}")

# # Descobrir o id de todos os programadores

# ocupacao_programador = srub.ocupacoes["programmer"]
# programadores = ocupacao_programador.usuarios
# print("ID dos programadores:", *map(lambda x: x.user_id, programadores))

# # Descobrir movie_id de todos os filmes de terror

# horror = srub.generos["Horror"]
# print("ID dos filmes de Horror:", *map(lambda x: x.movie_id, horror.filmes))

# # Listar o nome dos filmes que são de Horror e ação

# action = srub.generos["Action"].filmes
# horror = srub.generos["Horror"].filmes


# def intersection(lst1, lst2):
#     lst3 = [value for value in lst1 if value in lst2]
#     return lst3


# action_horror = intersection(action, horror)

# for filme in action_horror:
#     print("Filme de Acao e Horror:", filme.movie_title)

# # Mostrar todas as avaliações do usuário 1, mostrar o movie_id e o rating

# user_id = "1"
# user = srub.usuarios[user_id]

# for aval in user.avaliacoes:
#     rating = aval.rating
#     movie_id = aval.filme.movie_id

#     print(f"Usuario {user_id} avaliou o filme {movie_id} com nota {rating}")
