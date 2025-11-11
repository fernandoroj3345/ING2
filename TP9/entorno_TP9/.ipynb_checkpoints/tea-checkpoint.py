# Datos
tasa_mensual = 0.07  # 7%
periodos_mes = 12    # meses al año

# Calcular la TEA
TEA = (1 + tasa_mensual) ** periodos_mes - 1

# Duración original del proyecto (meses)
meses = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

duracion_proyecto = meses[-1]

print(f"Tasa Efectiva Anual (TEA): {TEA:.4f} o {TEA*100:.2f}%")
print(f"Duración del proyecto: {duracion_proyecto} meses")

# Nota: para ruta crítica (camino crítico) se requiere info de tareas y dependencias,
# con solo esfuerzo mensual es insuficiente para recalcularla sin más datos.
