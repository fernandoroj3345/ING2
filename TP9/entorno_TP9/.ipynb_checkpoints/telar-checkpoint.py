# Datos de la inversión
inversion = 1000
rendimiento_ganancia = 0.07 * inversion  # 7% de ganancia mensual
# Rendimiento en pérdida se asume pérdida total de la inversión

# Ecuación de esperanza nula:
# Pg * ganancia + Pp * (-inversión) = 0
# Pp = 1 - Pg

# Calculo Pg
Pg = inversion / (inversion + rendimiento_ganancia)
Pp = 1 - Pg

print(f"Probabilidad de ganar (Pg): {Pg:.4f} (~{Pg*100:.2f}%)")
print(f"Probabilidad de perder (Pp): {Pp:.4f} (~{Pp*100:.2f}%)")
