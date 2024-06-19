import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

# Carregar o arquivo CSV
data = pd.read_csv("Breast_cancer_data.csv")

# Mostrar as primeiras 10 linhas do dataframe
print(data.head(10))

# Plotar o histograma da coluna "diagnosis"
plt.figure(figsize=(10, 6))
data["diagnosis"].hist()
plt.title("Histograma de Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Frequência")
plt.show()

# Calcular a correlação
corr = data.iloc[:,:-1].corr(method="pearson")

# Plotar o heatmap da correlação
plt.figure(figsize=(12, 10))
cmap = sns.diverging_palette(250, 354, 80, 60, center='dark', as_cmap=True)
sns.heatmap(corr, vmax=1, vmin=-.5, cmap=cmap, square=True, linewidths=.2)
plt.title("Mapa de Calor da Correlação")
plt.show()
