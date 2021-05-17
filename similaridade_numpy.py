import numpy as np
from numpy import linalg as LA

a = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])


def cos_similarity(a: np.ndarray, b: np.ndarray) -> float:
    dot = a @ b
    normA = LA.norm(a)
    normB = LA.norm(b)

    return dot / (normA * normB)


linha0 = a[0, :]
linha2 = a[2, :]

print(cos_similarity(linha0, linha2))

coluna0 = a[:, 0]
coluna2 = a[:, 2]

print(cos_similarity(coluna0, coluna2))
