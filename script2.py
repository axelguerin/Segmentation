from sklearn_som.som import SOM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Chargement des données
iris_df = pd.read_csv("iris.csv")
iris_data = iris_df.iloc[:, :4].values
iris_label = iris_df.iloc[:, 4].values

result = [0, 0, 0]
ct = 0
for i in range(1000):
    som = SOM(m = 3, n = 1, dim = 4)
    som.fit(iris_data)
    predictions_som = som.predict(iris_data)
    cluster = predictions_som[0]
    b = True 
    for i in range(50):
        b = b and (cluster == predictions_som[i])
    if b:
        ct += 1
    result[cluster] += 1

print(result)
print(ct)
