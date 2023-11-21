import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Criando valores para os eixos x e y
# x = np.array([1, 2, 3, 4, 5, 6, 10, 11, 12])
x1 = np.array(np.random.randint(1, 1000, 500))
x1 = np.sort(x1)
y = x1**2

# Setando as legendas dos eixos x e y
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# Plotando o gráfico e customizando o gráfico
plt.plot(x1, y, 'o:', linewidth = 3, color = 'green')
plt.show()

# ------------------------------------------------------

xx1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
yy1 = xx1**2

yy2 = xx1

# Plotando 2 gráficos
# 1º param: x, y e estilo do primeiro grafico; 2º param: x, y e estilo do segundo gráfico
plt.plot(xx1, yy1, 'r-', xx1, yy2, 'b--')
plt.show()

# ------------------------------------------------------


# Plotando Subplots
xxx1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
yyy1 = xxx1**2
yyy2 = xxx1*2

# Params:
# nº de linhas do subplot
# quantas colunas
# posicao
plt.subplot(1, 2, 1)
plt.title('Exponencial')
plt.plot(xxx1, yyy1, 'r-')

plt.subplot(1, 2, 2)
plt.title('Linear')
plt.plot(xxx1, yyy2, 'b--')

plt.show()

# ------------------------------------------------------

# Uma plotagem sobre o dataset paises.csv
# Qual é a renda per capita dos 6 maiores paises do planeta?
dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Extraindo os 6 maiores paises
dfPaises2 = dfPaises.nlargest(6, 'Area (sq. mi.)')

# Plotando os paises
# Params:
# eixo x - nome dos paises
# eixo y - renda per capita dos paises
# tamanho das bolinhas - tamanho dos paises
plt.scatter(dfPaises2['Country'], dfPaises2['GPD ($ per capita)'], s=dfPaises2['Area (sq.mi.)']/10000)

plt.show()

