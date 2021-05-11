
class Occupation:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.usuarios = {}

    def inserir_usuario(self, user):
        self.usuarios[user.user_id] = user

    def rating_medio(self):
        soma = 0
        qtd = 0
        for user_id in self.usuarios:
            user = self.usuarios[user_id]
            soma += user.rating_medio()
            qtd += 1
        return soma / qtd
