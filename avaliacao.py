
class Avaliacao:
    def __init__(self, rating, timestamp, usuario, filme) -> None:
        self.rating = float(rating)
        self.timestamp = timestamp
        self.usuario = usuario
        self.filme = filme
