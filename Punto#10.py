import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
R_squared = 0.9
S_x_squared = 8
X = 2

# Calcular la varianza de la suma de las variables
Var_X_plus_Y = S_x_squared + (1 - R_squared) * X**2

# Crear un conjunto de datos para X
X_values = np.linspace(-5, 5, 100)

# Calcular la regresión lineal y la recta de regresión
Y_values = X_values * np.sqrt(R_squared) * np.sqrt(S_x_squared)  # Recta de regresión

# Graficar la recta de regresión
plt.plot(X_values, Y_values, label='Recta de Regresión')

# Etiquetas y título
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión Lineal')

# Puntos de datos
plt.scatter(X, X * np.sqrt(R_squared) * np.sqrt(S_x_squared), color='red', label='Punto de Datos')

# Leyenda
plt.legend()

# Mostrar la gráfica
plt.show()

print(f"Varianza de la suma de X e Y: {Var_X_plus_Y}")
