# Script para calcular la esperanza matemática de apostar a color en ruleta europea con cero verde

# Parámetros del juego
apuesta = 1000              # Valor de la ficha mínima en pesos
n_numeros = 37              # Total de casillas (36 números + cero verde)
n_colores = 18              # Cantidad de casillas por color (rojo o negro)
n_perder = n_numeros - n_colores  # Incluye el color opuesto y el cero

# Probabilidades
prob_ganar = n_colores / n_numeros
prob_perder = n_perder / n_numeros

# Pagos
ganancia = apuesta  # Si se acierta color, se gana lo apostado además de la devolución de la apuesta
perdida = -apuesta  # Si no se acierta color, se pierde lo apostado

# Esperanza matemática
esperanza = prob_ganar * ganancia + prob_perder * perdida

# Mostrar resultados
print(f"La probabilidad de ganar es {prob_ganar:.4f}")
print(f"La probabilidad de perder es {prob_perder:.4f}")
print(f"La esperanza matemática por cada apuesta de ${apuesta} es ${esperanza:.2f}")

# Resultado esperado:
# La esperanza será negativa (se esperará perder dinero en promedio)
