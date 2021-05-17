from abc import ABC, abstractmethod
import numpy as np


class Estatistica(ABC):

    @abstractmethod
    def as_array(self) -> np.ndarray:
        pass

    def dados_estatisticos(self):
        array_rating = self.as_array()
        media = array_rating.mean()
        desvio = array_rating.std()
        variancia = array_rating.var()
        return {"mean": media, "std": desvio, "var": variancia}
