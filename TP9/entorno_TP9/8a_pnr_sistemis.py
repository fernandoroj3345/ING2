# PNR_sistemis.py modificado para Ingeniería de Software II
# Modelo dinámico Putnam-Norden-Rayleigh (PNR) usando datos históricos

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ======= DATOS HISTÓRICOS DEL PROYECTO =======
# Este bloque carga los datos de esfuerzo por mes extraídos de la imagen
t_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])            # Vector de meses
E_data = np.array([8, 21, 25, 30, 25, 24, 17, 15, 11])    # Esfuerzo instantáneo por mes, en personas-mes

# Muestra los datos en consola para verificación
df = pd.DataFrame({'Meses': t_data, 'PM': E_data})
print('Datos históricos de calibración:')
print(df)

# ======= CÁLCULO DEL ESFUERZO TOTAL =======
# Suma el esfuerzo total para el proyecto, necesario para calibrar el modelo
K = np.sum(E_data)
print(f"\nEl esfuerzo total del proyecto es K={K} PM")

# ======= DEFINICIÓN DE LA FUNCIÓN DE AJUSTE =======
# La función del modelo PNR, parametrizada (a: factor de dispersión)
def modelo_pnr(t, a):
    return 2 * K * a * t * np.exp(-a * t**2)

# ======= AJUSTE DEL MODELO A LOS DATOS =======
# Ajusta el parámetro 'a' utilizando el histórico con curve_fit (mejor ajuste)
popt, pcov = curve_fit(modelo_pnr, t_data, E_data, p0=[0.1])  # Supone a~0.1 inicial
a_estimada = popt[0]
print(f"\nParámetro a ajustado por mejor calibración: a = {a_estimada:.4f}")

# ======= GENERACIÓN DE CURVAS MODELO Y OBSERVADOS =======
# Crea vectores de tiempo para graficar el mejor ajuste
t_fit = np.linspace(min(t_data), max(t_data), 100)
E_fit = modelo_pnr(t_fit, a_estimada)

# ======= GRÁFICA DE DATOS Y MODELO =======
# - Puntos azules: histórico observado
# - Línea roja: curva mejor ajustada (modelo PNR)
plt.scatter(t_data, E_data, label='Histórico observado', color='blue')
plt.plot(t_fit, E_fit, label='Modelo PNR ajustado', color='red')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (personas-mes)')
plt.title('Calibración PNR: histórico vs modelo ajustado')
plt.legend()
plt.show()

# ======= CURVA DEL PROYECTO MODIFICADO SEGÚN UN K ESPECIFICADO =======
# Si el usuario ingresa un nuevo esfuerzo (Kp), genera una curva alternativa
Kp = 120  # Modifica este valor para el esfuerzo aceptar por parte del alumno
E_fit_proyecto = 2 * Kp * a_estimada * t_fit * np.exp(-a_estimada * t_fit**2)

# Agrega ambas curvas y los datos al gráfico comparativo
plt.scatter(t_data, E_data, label='Histórico observado', color='blue')
plt.plot(t_fit, E_fit, label=f'Modelo ajustado (K={K})', color='red')
plt.plot(t_fit, E_fit_proyecto, label=f'Proyecto Modificado (K={Kp})', color='green')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (personas-mes)')
plt.title('PNR: Datos vs ajuste y proyecto aceptado')
plt.legend()
plt.show()

# ======= BREVE EXPLICACIÓN DE CADA BLOQUE =======
# - Se cargan los datos del historial del proyecto (esfuerzo por mes) del archivo.
# - Se calcula el esfuerzo total del proyecto histórico.
# - Se ajusta el modelo matemático de Putnam-Rayleigh (PNR) a los datos.
# - Se grafican los datos observados y la curva ajustada.
# - Se permite comparar la curva original y una curva alternativa para un nuevo esfuerzo total (Kp).
