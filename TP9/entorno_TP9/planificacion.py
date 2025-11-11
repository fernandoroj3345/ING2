import numpy as np
import matplotlib.pyplot as plt

# Definición de las funciones dadas
def calcular_esfuerzo(S):
    return 8 * S**0.95

def calcular_tiempo_calendario(E):
    return 2.4 * E**0.33

# Intervalos especificados
S = np.linspace(0, 10000, 500)  # Tamaño del proyecto de 0 a 10000
E = calcular_esfuerzo(S)

# Para el tiempo calendario, el intervalo de esfuerzos es [1, 500]
E_td = np.linspace(1, 500, 500)
td = calcular_tiempo_calendario(E_td)

# Graficar esfuerzo vs tamaño
plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
plt.plot(S, E, label='Esfuerzo E')
plt.title('Esfuerzo (E) vs Tamaño del proyecto (S)')
plt.xlabel('Tamaño del proyecto S')
plt.ylabel('Esfuerzo E')
plt.grid(True)
plt.legend()

# Graficar tiempo calendario vs esfuerzo
plt.subplot(1, 2, 2)
plt.plot(E_td, td, 'r', label='Tiempo calendario td')
plt.title('Tiempo calendario (td) vs Esfuerzo (E)')
plt.xlabel('Esfuerzo E')
plt.ylabel('Tiempo calendario td')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

