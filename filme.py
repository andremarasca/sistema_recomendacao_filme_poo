class Filme:
    def __init__(self, nome: str, data_lancamento: str) -> None:
        self.nome = nome
        self.data_lancamento = data_lancamento
        self.generos = []
        self.avaliacoes = []

    def inserir_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def inserir_genero(self, genero):
        self.generos.append(genero)
