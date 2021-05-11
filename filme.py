class Filme:
    def __init__(self, movie_id, movie_title, release_date, video_release_date, IMDb_URL) -> None:
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.release_date = release_date
        self.video_release_date = video_release_date
        self.IMDb_URL = IMDb_URL
        self.generos = []
        self.avaliacoes = {}

    def inserir_avaliacao(self, avaliacao):
        self.avaliacoes[avaliacao.usuario.user_id] = avaliacao

    def inserir_genero(self, genero):
        self.generos.append(genero)

    def rating_medio(self):
        soma = 0
        qtd = 0
        for user_id in self.avaliacoes:
            soma += self.avaliacoes[user_id].rating
            qtd += 1
        return soma / qtd
