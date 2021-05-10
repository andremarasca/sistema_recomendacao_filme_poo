from abc import ABC, abstractmethod


class AlgoritmoDistancia(ABC):
    @abstractmethod
    def calcula_distancia(self, item1, item2):
        pass


class DistanciaCosseno(AlgoritmoDistancia):
    def dot_product(self, a: list = [], b: list = []) -> float:
        dot = 0
        length = len(a)
        for i in range(length):
            dot += a[i]*b[i]
        return dot

    def norm_l2(self, a: list = []) -> float:
        norm = 0
        length = len(a)
        for i in range(length):
            norm += a[i]**2

        return (norm)**0.5

    def cos_similarity(self, a: list = [], b: list = []) -> float:
        dot = self.dot_product(a, b)
        normA = self.norm_l2(a)
        normB = self.norm_l2(b)

        return dot / (normA * normB)

    @classmethod
    def calcula_distancia(cls, item1, item2):
        return cls.cos_similarity(item1, item2)


class CorrelacaoDePearson(AlgoritmoDistancia):

    def average(self, x: list = []) -> float:
        assert len(x) > 0
        return float(sum(x)) / len(x)

    def pearson_def(self, x: list = [], y: list = []) -> float:
        assert len(x) == len(y)
        n = len(x)
        assert n > 0
        avg_x = self.average(x)
        avg_y = self.average(y)
        diffprod = 0
        xdiff2 = 0
        ydiff2 = 0
        for idx in range(n):
            xdiff = x[idx] - avg_x
            ydiff = y[idx] - avg_y
            diffprod += xdiff * ydiff
            xdiff2 += xdiff * xdiff
            ydiff2 += ydiff * ydiff

        return diffprod / ((xdiff2 * ydiff2) ** (0.5))

    @classmethod
    def calcula_distancia(cls, item1, item2):
        return cls.pearson_def(item1, item2)
