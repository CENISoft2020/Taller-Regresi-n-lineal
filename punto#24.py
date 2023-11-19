import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
x = 8
y = 21
Sx = 2
Sy_squared = 18
Mxy = 3.6

# Cálculo de los coeficientes de la recta de regresión
b = Mxy / Sx**2
a = y - b * x

# Ecuación de la recta de regresión
def regression_line(X):
    return a + b * X

# Generar puntos para la recta de regresión
X_regression = np.linspace(min(x - 2*Sx, 0), max(x + 2*Sx, 10), 100)
Y_regression = regression_line(X_regression)

# Graficar los puntos de datos
plt.scatter(x, y, color='red', label='Datos (8, 21)')

# Graficar la recta de regresión
plt.plot(X_regression, Y_regression, label=f'Recta de Regresión: Y = {a:.2f} + {b:.2f}X', color='blue')

# Etiquetas y título
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Recta de Regresión Lineal y Datos')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()
