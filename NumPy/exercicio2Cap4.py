## Juan Carlos GES 41
import numpy as np

### Questão 1
print("Questão 1")
np.random.seed(5)

arrayFloats = np.random.randn(10)
arrayFloats = arrayFloats * 100
posArrayFloats = arrayFloats.astype(int)
print(arrayFloats)
print(posArrayFloats)
print("------------------------------")


### Questão 2
print("\nQuestão 2")
np.random.seed(10)

mat44 = np.random.randint(1, 50, (4,4))
print(mat44)
print("------------------------------")


### Questão 3
print("\nQuestão 3")

print("Média linha 0: ", mat44.mean(axis=1)[0])
print("Média linha 1: ", mat44.mean(axis=1)[1])
print("Média linha 2: ", mat44.mean(axis=1)[2])
print("Média linha 3: ", mat44.mean(axis=1)[3])
print("Média coluna 0: ", mat44.mean(axis=0)[0])
print("Média coluna 1: ", mat44.mean(axis=0)[1])
print("Média coluna 2: ", mat44.mean(axis=0)[2])
print("Média coluna 3: ", mat44.mean(axis=0)[3])

print("Maior valor de média linha: ", max(mat44.mean(axis=1)))
print("Menor valor de média coluna: ", max(mat44.mean(axis=0)))
print("------------------------------")


### Questão 4
print("\nQuestão 4")
numbers = np.unique(mat44)
countNumbers = np.unique(mat44, return_counts=True)[1].tolist()

print("Os números", np.unique(mat44), "apareceram", np.unique(mat44, return_counts=True)[1], "vezes respectivamente")

pos = 0
print("Os números que aparecem apenas 2x são:", end=' ')
for n in countNumbers:
    if n == 2:
        print(numbers[pos], end=' ')
    pos += 1
