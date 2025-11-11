# Parámetros
valor_futuro = 1000       # Monto que se recibirá en un año
tasa_mensual = 0.07       # Tasa de interés mensual
periodos = 12             # Meses en un año

# Cálculo del valor presente (descuento compuesto)
valor_presente = valor_futuro / (1 + tasa_mensual) ** periodos

print(f"El valor presente de la inversión es: ${valor_presente:.2f}")
