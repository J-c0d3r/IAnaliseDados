## Juan Carlos GES 41
from array import array
from operator import concat

import numpy as np

## Questao 1
print("Questão 1")
tam21 = np.linspace(0, 1, 21)
print(tam21)

print("\n--------------------------------------------------\n")

## Questao 2
print("Questão 2")
par1 = np.arange(0, 51, 2)
print("0 até 51: ", par1)
print()
par2 = np.arange(100, 50, -2)
print("100 até 50: ", par2)
print()
concatenado = np.concatenate((par1, par2))
print("Concatenado: ", concatenado)
print()
ordenado = np.sort(concatenado)
print("Resultado final(ordenado): ", ordenado)

print("\n--------------------------------------------------\n")

## Questao 3
print("Questão 3")
resultDesc = np.flip(ordenado)
print("Decrescente: ", resultDesc)

print("\n--------------------------------------------------\n")

## Questao 4
print("Questão 4")
tresQuarto = np.ones((3,4))
print(tresQuarto, "\n")
array1D = tresQuarto.reshape(1,12)
print(array1D)

print("\n--------------------------------------------------\n")

## Questao 5
print("Questão 5")
tamQualquer = np.array([[6,8,3], [10,5,22], [5,5,5]])
print(tamQualquer)
linhas, colunas = tamQualquer.shape
if ((linhas*colunas)%2 == 0):
    print("Essa matriz é capaz de se tornar um vetor com tamanho par")
else:
    print("Essa matriz é capaz de se tornar um vetor com tamanho impar")
