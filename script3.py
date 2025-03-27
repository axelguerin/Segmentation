from sklearn_som.som import SOM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Chargement des données
iris_df = pd.read_csv("iris.csv")
iris_data = iris_df.iloc[:, :4].values
iris_label = iris_df.iloc[:, 4].values

# Initialisation SOM

grid_size = 10
som = SOM(m = grid_size, n = grid_size, dim = 4)
som.fit(iris_data)

# Visualisation

predictions_som = som.predict(iris_data)
grid = np.zeros((grid_size, grid_size))
plt.figure(figsize = (10, 10))

for idx, pred in enumerate(predictions_som):
    x, y = pred //grid_size, pred % grid_size
    if iris_label[idx] == 'setosa': 
        color = 'red'
    if iris_label[idx] == 'versicolor':
        color = 'blue' 
    if iris_label[idx] == 'virginica':
        color = 'green'
    plt.plot(x, y, marker = 'o', color = color, markersize = 20)

plt.title('Grille SOM')
plt.xlim([-1, grid_size])
plt.ylim([-1, grid_size])
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()