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

print("="*50)
# %%

srib = SistemaRecomendacaoItemBased(
    "ml-100k/u.user", "ml-100k/u.genre", "ml-100k/u.item", "ml-100k/u.data")

rating = srib.estimate_target_rating(
    n_neighbors=3, target_movie_id="1", target_user_id="3")

print("Rating Item-Based:", rating)
print("="*50)
# %% Estimar o rating que o usuario alvo daria para o filme alvo se ele assistisse esse filme

srub = SistemaRecomendacaoUserBased(
    "ml-100k/u.user", "ml-100k/u.genre", "ml-100k/u.item", "ml-100k/u.data")

rating = srub.estimate_target_rating(
    n_neighbors=3, target_movie_id="1", target_user_id="3")

print("Rating User-Based:", rating)
print("="*50)
# %% Testes de acesso

# Imprimir 5 avaliações do usuário 100.

user_id = "100"
user: Usuario = srub.usuarios[user_id]

i = 0
for movie_id in user.avaliacoes:
    avaliacao: Avaliacao = user.avaliacoes[movie_id]
    rating = avaliacao.rating
    filme: Filme = avaliacao.filme
    movie_title = filme.movie_title
    print(
        f"Usuario {user_id} avaliou com nota {rating} o filme '{movie_title}'")
    i += 1
    if i == 5:
        break

print("="*50)

# Descobrir os generos do filme 123

movie_id = "123"
movie = srub.filmes[movie_id]
generos = movie.generos
for genero in generos:
    print(f"Filme {movie_id} tem genero {genero.nome}")

print("="*50)

# Descobrir o id de todos os programadores

ocupacao_programador = srub.ocupacoes["programmer"]
programadores = ocupacao_programador.usuarios  # dicionario
print("ID dos programadores:", list(programadores.keys()))

print("="*50)

# Descobrir movie_id de todos os filmes de terror

horror = srub.generos["Horror"]
print("ID dos filmes de Horror:", list(horror.filmes.keys()))

print("="*50)

# Listar o nome dos filmes que são de Horror e ação

action = srub.generos["Action"].filmes
horror = srub.generos["Horror"].filmes

for movie_id in action:
    if movie_id in horror:
        print("Filme de Acao e Horror:", action[movie_id].movie_title)

print("="*50)

# Imprimir rating médio do usuario 100

print("Rating medio do user 100:", srub.usuarios["100"].rating_medio())
print("="*50)

# Imprimir rating médio do filme 100

print("Rating medio do filme 100:", srub.filmes["100"].rating_medio())
print("="*50)

# Imprimir rating médio do genero Horror

print("Rating medio do genero horror:", srub.generos["Horror"].rating_medio())
print("="*50)

# Imprimir rating médio da ocupação programador

ocupacao_programador = srub.ocupacoes["programmer"]
print("Rating medio da ocupacao programador:",
      ocupacao_programador.rating_medio())
print("="*50)
