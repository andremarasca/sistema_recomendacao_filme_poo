import numpy as np
from sistema_recomendacao_user_based import SistemaRecomendacaoUserBased

my_data = np.genfromtxt('ml-100k/u.data', delimiter='\t')

srub = SistemaRecomendacaoUserBased()
