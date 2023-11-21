import numpy as np

teste = np.array([[1,2,3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(type(teste))
print(teste[2][1])
print(teste[1][0])

teste2 = np.zeros(2)
print(teste2)

teste3 = np.ones(3)
print(teste3)

teste4 = np.arange(15)
print(teste4)

teste5 = np.arange(1, 20, 2)
print(teste5)

teste6 = np.linspace(1, 20, 3)
print(teste6)

print("-------------")

des = np.array([5,8,3,7,1,0,3,4,2])
print(des)

cres = np.sort(des)
print(cres)
decr = np.flip(cres)
print(decr)

together = np.concatenate((teste4, cres))
print(type(together))
print(together)

print("-------------")

mtz = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(mtz)
print("Quantidade de elementos do array: ", mtz.size)
print("Dimensões: ", mtz.ndim)
print("teste: ", mtz.shape)

print("-------------")

shape = np.array([1,2,3,4,5,6])
print(shape)
reshape = shape.reshape(6,1)
print(reshape)




