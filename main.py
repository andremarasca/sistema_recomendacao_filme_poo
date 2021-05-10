from genero import Genero
from usuario import Usuario
from filme import Filme
from avaliacao import Avaliacao

genero1 = Genero("Comédia")
genero2 = Genero("Terror")
genero3 = Genero("Ação")

user1 = Usuario(0, 20, "Estudante", 88888888)
user2 = Usuario(1, 25, "Engenheiro", 88888887)
user3 = Usuario(2, 90, "Aposentado", 88888899)

filme1 = Filme("Godzila", "01/01/2000")
filme2 = Filme("O sapateiro", "01/01/2012")
filme3 = Filme("Avengers", "01/06/2015")

filme1.inserir_genero(genero1)
filme1.inserir_genero(genero2)
filme2.inserir_genero(genero2)
filme3.inserir_genero(genero3)

avaliacao1 = Avaliacao(4, user1, filme1)
user1.inserir_avaliacao(avaliacao1)
filme1.inserir_avaliacao(avaliacao1)

avaliacao2 = Avaliacao(3, user2, filme1)
user2.inserir_avaliacao(avaliacao1)
filme1.inserir_avaliacao(avaliacao1)
