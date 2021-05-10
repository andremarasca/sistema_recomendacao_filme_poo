from genero import Genero
from occupation import Occupation
from usuario import Usuario
from filme import Filme
from avaliacao import Avaliacao
from read_dataset import read_dataset


class DadosNaoImportados(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class SistemaRecomendacaoUserBased:
    def __init__(self, user_filename, genre_filename, item_filename, data_filename) -> None:
        self.usuarios = {}
        self.filmes = {}
        self.generos = {}
        self.ocupacoes = {}

        user_header = "user_id|age|gender|occupation|zip_code"
        user_header = user_header.split("|")
        dataset_user = read_dataset(
            user_filename, sep="|", header=user_header)

        genre_header = "genre|genre_id"
        genre_header = genre_header.split("|")
        dataset_genre = read_dataset(
            genre_filename, sep="|", header=genre_header)

        item_header = "movie_id|movie_title|release_date|video_release_date|IMDb_URL|unknown|Action|Adventure|Animation|Children's|Comedy|Crime|Documentary|Drama|Fantasy|Film-Noir|Horror|Musical|Mystery|Romance|Sci-Fi|Thriller|War|Western"
        item_header = item_header.split("|")
        dataset_movie = read_dataset(
            item_filename, sep="|", header=item_header)

        data_header = "user_id|item_id|rating|timestamp"
        data_header = data_header.split("|")
        dataset_data = read_dataset(
            data_filename, sep="\t", header=data_header)

        self.importar_dados_usuarios(dataset_user)
        self.importar_dados_genero(dataset_genre)
        self.importar_dados_filmes(dataset_movie)
        self.importar_dados_avaliacoes(dataset_data)

    def inserir_occupation(self, occupation: str):
        if occupation not in self.ocupacoes:
            self.ocupacoes[occupation] = Occupation(occupation)

    def inserir_genre(self, genre: str):
        if genre not in self.generos:
            self.generos[genre] = Genero(genre)

    def importar_dados_genero(self, dataset_genre):
        for genre in dataset_genre["genre"]:
            self.inserir_genre(genre)

    def importar_dados_filmes(self, dataset_movie):
        "movie_id|movie_title|release_date|video_release_date|IMDb_URL"
        for idx in range(len(dataset_movie["movie_id"])):
            movie_id = dataset_movie["movie_id"][idx]
            movie_title = dataset_movie["movie_title"][idx]
            release_date = dataset_movie["release_date"][idx]
            video_release_date = dataset_movie["video_release_date"][idx]
            IMDb_URL = dataset_movie["IMDb_URL"][idx]

            movie = Filme(movie_id, movie_title, release_date,
                          video_release_date, IMDb_URL)

            for genre in self.generos:
                if dataset_movie[genre][idx] == "1":
                    obj_genre: Genero = self.generos[genre]
                    movie.inserir_genero(obj_genre)
                    obj_genre.inserir_filme(movie)

            self.filmes[movie_id] = movie

    def importar_dados_usuarios(self, dataset_user):
        for idx in range(len(dataset_user["user_id"])):
            user_id = dataset_user["user_id"][idx]
            age = dataset_user["age"][idx]
            gender = dataset_user["gender"][idx]
            occupation = dataset_user["occupation"][idx]
            zip_code = dataset_user["zip_code"][idx]

            self.inserir_occupation(occupation)
            obj_occupation: Occupation = self.ocupacoes[occupation]

            user = Usuario(user_id, int(age), gender, obj_occupation, zip_code)
            obj_occupation.inserir_usuario(user)

            self.usuarios[user_id] = user

    def importar_dados_avaliacoes(self, dataset_data):
        for idx in range(len(dataset_data["user_id"])):
            user_id = dataset_data["user_id"][idx]
            item_id = dataset_data["item_id"][idx]
            rating = dataset_data["rating"][idx]
            timestamp = dataset_data["timestamp"][idx]

            usuario: Usuario = self.usuarios[user_id]
            filme: Filme = self.filmes[item_id]

            avaliacao = Avaliacao(rating, timestamp, usuario, filme)
            usuario.inserir_avaliacao(avaliacao)
            filme.inserir_avaliacao(avaliacao)
