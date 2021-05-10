
class Occupation:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.usuarios = []

    def inserir_usuario(self, filme):
        self.usuarios.append(filme)
