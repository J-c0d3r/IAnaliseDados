# AULA 2 - NUMPY
import numpy as np

# LIDAR COM NUMEROS ALEATORIOS
# semente de dados
np.random.seed(10)
# rand - geracao de numeros float
arr = np.random.rand(6)
# broadcasting - a possibilidade de operações entre escalares e vetores
print(arr * 100)
# randint
arr2 = np.random.randint(1, 100, 10)
print(arr2)

# EXTRAINDO ELEMENTOS UNICOS DE UMA COLECAO
np.random.seed(10)
arr5 = np.random.randint(1, 10, 10)
print(arr5)
print(np.unique(arr5, return_counts=True))
arr7 = np.unique(arr5, return_counts=True)
print(arr7[1])
print(np.unique(arr5, return_counts=True)[1])

# OPERACOES COM COLECOES NO PYTHON
arr10 = np.arange(1, 5, 1)
arr11 = np.arange(5, 9, 1)
print(arr10, arr11)

print(arr10 * arr11)

# CRIANDO UM ARRAY 2-D
mtz = np.arange(9).reshape(3, 3)
print(mtz)
print(mtz.sum(axis=1)[2])