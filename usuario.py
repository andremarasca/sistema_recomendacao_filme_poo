from metricas_similaridade import DistanciaCosseno


class Usuario:
    def __init__(self, user_id: str, age: int, gender: str, occupation, zip_code: str) -> None:
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.zip_code = zip_code
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
