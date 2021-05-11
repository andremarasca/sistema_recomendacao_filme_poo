class Genero:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.filmes = {}

    def inserir_filme(self, filme):
        self.filmes[filme.movie_id] = filme

    def rating_medio(self):
        soma = 0
        qtd = 0
        for movie_id in self.filmes:
            movie = self.filmes[movie_id]
            soma += movie.rating_medio()
            qtd += 1
        return soma / qtd
