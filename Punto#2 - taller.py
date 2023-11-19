import numpy as np
import matplotlib.pyplot as plt

# Ecuaciones de las rectas de regresión mínimos cuadrados
def regression_line1(x):
    return -4 * x + 1/2

def regression_line2(x):
    return -16/9 * x + 1/9

# Valores x para el gráfico
x_values = np.linspace(-2, 2, 100)

# Calcular los valores y correspondientes a las rectas
y_values1 = regression_line1(x_values)
y_values2 = regression_line2(x_values)

# Gráfico de las rectas
plt.plot(x_values, y_values1, label='8x + 2y = 1')
plt.plot(x_values, y_values2, label='16x + 9y = 1')

# Etiquetas y título
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rectas de Regresión Mínimos Cuadrados')

# Leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
