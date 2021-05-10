from sistema_recomendacao_user_based import SistemaRecomendacaoUserBased

srub = SistemaRecomendacaoUserBased(
    "ml-100k/u.user", "ml-100k/u.genre", "ml-100k/u.item", "ml-100k/u.data")

# Acessar a primeira avaliação a lista do usuário 100, mostrar o movie_id e o rating

use_id = "100"
user = srub.usuarios[use_id]
aval = user.avaliacoes[0]
rating = aval.rating
movie_id = aval.filme.movie_id

print(f"Usuario {use_id} avaliou o filme {movie_id} com nota {rating}")

# Descobrir os generos do filme 123

movie_id = "123"
movie = srub.filmes[movie_id]
generos = movie.generos
for genero in generos:
    print(f"Filme {movie_id} tem genero {genero.nome}")

# Descobrir o id de todos os programadores

ocupacao_programador = srub.ocupacoes["programmer"]
programadores = ocupacao_programador.usuarios
print("ID dos programadores:", *map(lambda x: x.user_id, programadores))

# Descobrir movie_id de todos os filmes de terror

horror = srub.generos["Horror"]
print("ID dos filmes de Horror:", *map(lambda x: x.movie_id, horror.filmes))
