import numpy as np
import matplotlib.pyplot as plt

# Fórmulas dadas
# Esfuerzo: E = 8 * S^0.95
# Tiempo calendario: td = 2.4 * E^0.33

# Intervalo de tamaños del proyecto
S = np.linspace(0, 10000, 500)
E = 8 * (S ** 0.95)

# Intervalo de esfuerzos
E_intervalo = np.linspace(1, 500, 500)
td = 2.4 * (E_intervalo ** 0.33)

# Gráfico del esfuerzo en función del tamaño
plt.figure(figsize=(10, 5))
plt.plot(S, E, label="Esfuerzo (E)", color="blue")
plt.xlabel("Tamaño del proyecto (S)")
plt.ylabel("Esfuerzo (E)")
plt.title("Esfuerzo vs Tamaño del Proyecto")
plt.grid(True)
plt.legend()
plt.show()

# Gráfico del tiempo calendario en función del esfuerzo
plt.figure(figsize=(10, 5))
plt.plot(E_intervalo, td, label="Tiempo calendario (td)", color="green")
plt.xlabel("Esfuerzo (E)")
plt.ylabel("Tiempo calendario (td)")
plt.title("Tiempo Calendario vs Esfuerzo")
plt.grid(True)
plt.legend()
plt.show()

# --- Extra: comparación de picos para a y 4a en modelo PNR ---
K = 72  # esfuerzo total de referencia
a = 0.1  # valor estimado

def E_max(K, a):
    return K * np.sqrt(2*a) * np.exp(-0.5)

t_pico = 1/np.sqrt(2*a)
E_pico = E_max(K, a)

# Con a cuadruplicado
a4 = 4*a
t_pico4 = 1/np.sqrt(2*a4)
E_pico4 = E_max(K, a4)

print(f"Con a={a:.3f}: t_pico={t_pico:.2f}, E_max={E_pico:.2f}")
print(f"Con a={a4:.3f}: t_pico={t_pico4:.2f}, E_max={E_pico4:.2f}")
