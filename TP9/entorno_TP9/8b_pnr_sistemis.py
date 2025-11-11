import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos históricos del proyecto (de la imagen)
t_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])           # Meses
E_data = np.array([8, 21, 25, 30, 25, 24, 17, 15, 11])   # Esfuerzo instantáneo en personas-mes

# Suma el esfuerzo total histórico
K_historico = np.sum(E_data)

# Define la función del modelo PNR con parámetro 'a' y esfuerzo total K
def modelo_pnr(t, a):
    return 2 * K_historico * a * t * np.exp(-a * t**2)

# Ajusta el parámetro 'a' para que el modelo se acomode al dataset histórico
a0 = 0.1  # Valor inicial para 'a'
popt, _ = curve_fit(modelo_pnr, t_data, E_data, p0=[a0])
a_estimada = popt[0]

# Define modelo con esfuerzo total parametrizable para graficar nuevos proyectos
def modelo_pnr_custom(t, a, K):
    return 2 * K * a * t * np.exp(-a * t**2)

# Esfuerzo total aceptado para nuevo proyecto
K_nuevo = 72

# Vector continuo de tiempo para gráficar las curvas suavizadas
meses = np.linspace(1, 9, 100)

# Curva modelo ajustado al dataset histórico
E_fit = modelo_pnr(meses, a_estimada)

# Curva para nuevo proyecto con K=72 PM
E_fit_nuevo = modelo_pnr_custom(meses, a_estimada, K_nuevo)

# Graficar los datos históricos, el modelo ajustado y el nuevo proyecto
plt.figure(figsize=(8, 5))
plt.scatter(t_data, E_data, color='blue', label='Datos históricos')
plt.plot(meses, E_fit, color='red', label=f'Modelo ajustado (K={K_historico})')
plt.plot(meses, E_fit_nuevo, color='green', label=f'Proyecto nuevo (K={K_nuevo})')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (personas-mes)')
plt.title('Distribución de esfuerzo en el tiempo')
plt.legend()
plt.tight_layout()
plt.show()
