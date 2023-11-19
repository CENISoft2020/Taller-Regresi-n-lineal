import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
n = 20
R_squared = 0.64

# Generar datos aleatorios para la regresión lineal
np.random.seed(42)
X = np.random.rand(n) * 10
Y = 3 * X + np.random.randn(n) * 2

# Calcular la recta de regresión
coefficients = np.polyfit(X, Y, 1)
polynomial = np.poly1d(coefficients)

# Calcular el coeficiente de determinación ajustado
adjusted_R_squared = 1 - (1 - R_squared) * ((n - 1) / (n - 2))

# Crear la gráfica
plt.scatter(X, Y, label='Datos observados')
plt.plot(X, polynomial(X), color='red', label='Recta de regresión')

plt.title('Regresión Lineal Simple')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Mostrar la gráfica
plt.show()

print(f'Coeficiente de determinación (R^2): {R_squared}')
print(f'Coeficiente de determinación ajustado: {adjusted_R_squared}')
