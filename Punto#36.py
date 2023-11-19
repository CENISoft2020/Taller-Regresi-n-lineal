import numpy as np
import matplotlib.pyplot as plt

# Datos dados
X_bar = 30
Sx_squared = 25
r = 0.80
Y_bar = 45
Sy_squared = 8

# a) Estimar el valor de X_bar cuando Y = 28
b1 = r * (np.sqrt(Sy_squared) / np.sqrt(Sx_squared))
b0 = Y_bar - b1 * X_bar

# Estimación de Y cuando X = 28
X_new = 28
Y_hat = b0 + b1 * X_new

# b) Determinar la varianza residual
s_squared = Sy_squared - b1**2 * Sx_squared

# Imprimir resultados
print("Estimación de X_bar cuando Y = 28:", Y_hat)
print("Varianza residual:", s_squared)

# Crear datos para la línea de regresión
X = np.linspace(X_bar - 2 * np.sqrt(Sx_squared), X_bar + 2 * np.sqrt(Sx_squared), 100)
Y_reg = b0 + b1 * X

# Crear gráfica de dispersión y línea de regresión
plt.scatter(X_bar, Y_bar, color='red', marker='o', label='Datos dados')
plt.scatter(X_new, Y_hat, color='blue', marker='o', label=f'Estimación (Y={Y_hat:.2f} cuando X={X_new})')
plt.plot(X, Y_reg, color='green', label='Línea de regresión')

# Configurar la gráfica
plt.title('Regresión Lineal Simple')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
