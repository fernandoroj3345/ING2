#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* EffortModel
#* Programa para procesar un modelo exponencial de esfuerzo en base a datos históricos
#* 
#* UADER - FCyT
#* Ingeniería de Software II
#*
#* Dr. Pedro E. Colla / Modificado para práctica con dataset LOC-Esfuerzo
#* copyright (c) 2023,2025
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
import numpy as np
import matplotlib.pyplot as plt

#*------------------------------------------------------------------------------------------------
#* Dataset histórico (LOC vs Esfuerzo en persona-mes)
#*------------------------------------------------------------------------------------------------
LOC = np.array([1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
Esfuerzo = np.array([2,3,5,7,11,13,17,19,23,29])

#*------------------------------------------------------------------------------------------------
#* Modelo exponencial obtenido previamente:
#*   E = 0.00068 * LOC^1.116
#*------------------------------------------------------------------------------------------------
def esfuerzo_modelo(loc):
    return 0.00068 * (loc**1.116)

#*------------------------------------------------------------------------------------------------
#* Estimación para LOC=9100
#*------------------------------------------------------------------------------------------------
loc_estimado = 9100
esf_estimado = esfuerzo_modelo(loc_estimado)
print(f"Estimación para LOC={loc_estimado}: Esfuerzo ≈ {esf_estimado:.2f} persona-mes")

#*------------------------------------------------------------------------------------------------
#* Graficar resultados
#*------------------------------------------------------------------------------------------------
loc_range = np.linspace(1000, 10000, 200)
esf_curve = esfuerzo_modelo(loc_range)

plt.figure(figsize=(8,5))
plt.scatter(LOC, Esfuerzo, color='blue', label='Datos históricos')
plt.plot(loc_range, esf_curve, color='green', label='Modelo exponencial ajustado')
plt.scatter([loc_estimado], [esf_estimado], color='red', s=100, zorder=5,
            label=f'Estimación LOC={loc_estimado}, E={esf_estimado:.2f}')
plt.xlabel('Complejidad [LOC]')
plt.ylabel('Esfuerzo (persona-mes)')
plt.title('Modelo exponencial vs datos históricos')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
