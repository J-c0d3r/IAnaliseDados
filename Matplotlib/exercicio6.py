### Juan Carlos GES 41
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### Questão 1
arrSpace = pd.read_csv(".\..\space.csv", delimiter=";")

qntdUSA = arrSpace[arrSpace['Location'].str.contains('USA') == True]['Company Name'].unique()
qntdChina = arrSpace[arrSpace['Location'].str.contains('China') == True]['Company Name'].unique()

paises = ['USA', 'China']
qntds = [len(qntdUSA), len(qntdChina)]

plt.bar(paises, qntds, width=0.9, color='blue')
plt.show()


### Questão 2
arrPaises = pd.read_csv(".\..\paises.csv", delimiter=";")

paisesNA = arrPaises[arrPaises["Region"].str.contains('NORTHERN AMERICA') == True]
plt.plot(paisesNA['Country'], paisesNA['Birthrate'], '-b', paisesNA['Country'], paisesNA['Deathrate'], '-r')

plt.legend(['Birthrate', 'Deathrate'])
plt.show()
