import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
sigma_ingresos = 3000
sigma_gastos = 2000
rho = 0.85

# Calcula la desviación típica de los ahorros
sigma_ahorros = np.sqrt(sigma_ingresos**2 + sigma_gastos**2 - 2 * rho * sigma_ingresos * sigma_gastos)

# Genera datos aleatorios para ingresos y gastos (usando una distribución normal)
np.random.seed(42)  # Para reproducibilidad
ingresos = np.random.normal(0, sigma_ingresos, 1000)
gastos = np.random.normal(0, sigma_gastos, 1000)

# Calcula los ahorros como la diferencia entre ingresos y gastos
ahorros = ingresos - gastos

# Grafica los datos
plt.figure(figsize=(10, 6))

plt.scatter(ingresos, gastos, label='Datos Aleatorios')
plt.xlabel('Ingresos')
plt.ylabel('Gastos')
plt.title('Relación entre Ingresos y Gastos')
plt.legend()
plt.grid(True)
plt.show()

# Grafica los ahorros
plt.figure(figsize=(10, 6))

plt.hist(ahorros, bins=30, edgecolor='black')
plt.xlabel('Ahorros')
plt.ylabel('Frecuencia')
plt.title('Distribución de Ahorros')
plt.grid(True)
plt.show()
