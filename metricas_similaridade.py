from abc import ABC, abstractmethod


class AlgoritmoDistancia(ABC):
    @abstractmethod
    def calcula_distancia(cls, item1, item2):
        pass


class DistanciaCosseno(AlgoritmoDistancia):
    @classmethod
    def dot_product(cls, a: list = [], b: list = []) -> float:
        dot = 0
        length = len(a)
        for i in range(length):
            dot += a[i]*b[i]
        return dot

    @classmethod
    def norm_l2(cls, a: list = []) -> float:
        norm = 0
        length = len(a)
        for i in range(length):
            norm += a[i]**2

        return (norm)**0.5

    @classmethod
    def cos_similarity(cls, a: list = [], b: list = []) -> float:
        dot = cls.dot_product(a, b)
        normA = cls.norm_l2(a)
        normB = cls.norm_l2(b)

        return dot / (normA * normB)

    @classmethod
    def calcula_distancia(cls, item1, item2):
        return cls.cos_similarity(item1, item2)


class CorrelacaoDePearson(AlgoritmoDistancia):
    @classmethod
    def average(cls, x: list = []) -> float:
        assert len(x) > 0
        return float(sum(x)) / len(x)

    @classmethod
    def pearson_def(cls, x: list = [], y: list = []) -> float:
        assert len(x) == len(y)
        n = len(x)
        assert n > 0
        avg_x = cls.average(x)
        avg_y = cls.average(y)
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
