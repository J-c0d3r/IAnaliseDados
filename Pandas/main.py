### Juan Carlos GES 41
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arrPaises = pd.read_csv('.\..\paises.csv', delimiter=";")

### Questão 1
## a)
print("Este são os países da OCEANIA: ")
print(arrPaises[arrPaises['Region'].str.contains('OCEANIA') == True]['Country'].sum())
print("---------------------------------------------------")

## b)
print("Quantidade total dos países pertencentes a OCEANIA:",
      len(arrPaises[arrPaises['Region'].str.contains('OCEANIA') == True]['Country'].sum()))
print("---------------------------------------------------")

### Questão 2
print("Média de alfabetização do mundo:", round(arrPaises['Literacy (%)'].mean(), 2), "%")
print("---------------------------------------------------")

### Questão 3
print(arrPaises[arrPaises['Population'] == np.max(arrPaises['Population'])][['Country', 'Region']])
print("---------------------------------------------------")

### Questão 4
result = arrPaises[arrPaises['Coastline (coast/area ratio)'] == 0]['Country']
result.to_csv('noCoast.csv', " ")
