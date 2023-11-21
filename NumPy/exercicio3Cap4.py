##Juan Carlos GES 41
import numpy as np

arrSpace = np.loadtxt('arquivos/space.csv', delimiter=';', dtype=str, encoding='utf-8')

print(type(arrSpace))

##Questao 1
# colunaStatus = arrSpace[1:, -1]
#
# qntdColunaStatus = len(colunaStatus)
#
# qntdOk = np.char.count(colunaStatus, 'Success').sum()
#
# valorFinal = round((qntdOk/qntdColunaStatus)*100, 2)
#
# print("Porcentagem de sucesso:", valorFinal , "%")


##Questao 2
# qntdCusto = arrSpace[1:, -2].astype(float)
#
# qntdCusto2 =  qntdCusto[qntdCusto > 0]
#
# somaCusto = qntdCusto2.sum()
# qntdTotalCusto = len(qntdCusto2)
#
# print("A média de gastos em missões com valores disponíveis é: US$", round(somaCusto/qntdTotalCusto, 2))


##Questao 3
# localizacao = arrSpace[1:, 2]
# totalUSA = np.char.count(localizacao, 'USA').sum()
#
# print("A quantidade total de missões feitas pelo USA foram:", totalUSA)


##Questao 4
# spaceX = arrSpace[arrSpace[:, 1] == 'SpaceX']
# maiorValor = np.max((spaceX[:, -2]).astype(float))
#
# maisCaroSpaceX = spaceX[(spaceX[:, -2]).astype(float) == maiorValor]
#
# print(maisCaroSpaceX)


##Questao 5
# empresas = np.unique(arrSpace[1:, 1])
#
# for empresa in empresas:
#     qntdMissoes = np.char.count(arrSpace[1:, 1], empresa).sum()
#     print(empresa, qntdMissoes)
