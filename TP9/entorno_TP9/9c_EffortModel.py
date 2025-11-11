#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* EffortModel - Comparación de estimaciones
#* Modelo exponencial basado en datos históricos LOC vs Esfuerzo
#* 
#* UADER - FCyT
#* Ingeniería de Software II
#*
#* Modificado para incluir estimaciones LOC=9100 y LOC=200
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
#* Modelo exponencial obtenido:
#*   E = 0.00068 * LOC^1.116
#*------------------------------------------------------------------------------------------------
def esfuerzo_modelo(loc):
    return 0.00068 * (loc**1.116)

#*------------------------------------------------------------------------------------------------
#* Estimaciones
#*------------------------------------------------------------------------------------------------
loc1, loc2 = 9100, 200
esf1, esf2 = esfuerzo_modelo(loc1), esfuerzo_modelo(loc2)

print(f"Estimación para LOC={loc1}: Esfuerzo ≈ {esf1:.2f} persona-mes")
print(f"Estimación para LOC={loc2}: Esfuerzo ≈ {esf2:.2f} persona-mes (extrapolación, baja confiabilidad)")

#*------------------------------------------------------------------------------------------------
#* Graficar resultados
#*------------------------------------------------------------------------------------------------
loc_range = np.linspace(500, 10500, 300)
esf_curve = esfuerzo_modelo(loc_range)

plt.figure(figsize=(9,6))
plt.scatter(LOC, Esfuerzo, color='blue', label='Datos históricos')
plt.plot(loc_range, esf_curve, color='green', label='Modelo exponencial ajustado')
plt.scatter([loc1], [esf1], color='red', s=100, zorder=5,
            label=f'Estimación LOC={loc1}, E={esf1:.2f}')
plt.scatter([loc2], [esf2], color='orange', s=100, zorder=5,
            label=f'Estimación LOC={loc2}, E={esf2:.2f} (extrapolación)')
plt.xlabel('Complejidad [LOC]')
plt.ylabel('Esfuerzo (persona-mes)')
plt.title('Estimaciones con modelo exponencial vs datos históricos')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
