import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
X = np.array([3, 5, 3, 2, 4, 1, 5, 2, 6, 3])
Y = np.array([2, 3, 5, 4, 6, 2, 5, 1, 3, 5])

# Calculando las medias
X_mean = np.mean(X)
Y_mean = np.mean(Y)

# Calculando la pendiente y la ordenada al origen
b = np.sum((X - X_mean) * (Y - Y_mean)) / np.sum((X - X_mean) ** 2)
a = Y_mean - b * X_mean

# Creando la recta de regresión
regression_line = a + b * X

# Estimando los costos para 10 sucursales
X_new = 10
Y_new = a + b * X_new

# Graficando los datos y la recta de regresión
plt.scatter(X, Y, label='Datos')
plt.plot(X, regression_line, color='red', label='Recta de Regresión')
plt.scatter(X_new, Y_new, color='green', label='Estimación para X=10')

# Etiquetas y leyenda
plt.xlabel('Número de sucursales')
plt.ylabel('Costos mensuales (millones de S.)')
plt.title('Regresión Lineal Simple')
plt.legend()

# Mostrando la gráfica
plt.show()
