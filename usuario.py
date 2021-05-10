from metricas_similaridade import DistanciaCosseno


class Usuario:
    def __init__(self, identificador: int, idade: int, ocupacao: str, zip: int) -> None:
        self.identificador = identificador
        self.idade = idade
        self.ocupacao = ocupacao
        self.zip = zip
        self.avaliacoes = []

    def inserir_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def classificar_filme(self, filme, nota: float):
        pass

    def recupera_classificacao(self) -> float:
        return 0

    def calcula_similaridade(self, outro_usuario) -> float:
        # return DistanciaCosseno.calcula_distancia(self, outro_usuario)
        return 0
