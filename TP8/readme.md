# Punto D cadena de comando

# Separación de responsabilidades: cada cuenta decide si procesa o delega.
# Extensible: poder agregar más cuentas fácilmente.
# Reutilizable y limpio: orientado a objetos y abierto a cambios futuros.

# Punto F se avanza a la version 1.2

# Iniciando versión 1.2
# Iniciando versión 1.2
# Pedido #1: Token=token1, Monto=$500
# Pedido #2: Token=token2, Monto=$500
# Pedido #3: Token=token1, Monto=$500
# Pedido #4: Token=token2, Monto=$500
# Pedido #5: Token=token2, Monto=$500
# Pedido #6: Token=token2, Monto=$500
# Pedido #7: No hay cuentas con saldo suficiente para $500
#
# Listado de pagos realizados:
# - Pedido #1: Token=token1, Monto=$500
# - Pedido #2: Token=token2, Monto=$500
# - Pedido #3: Token=token1, Monto=$500
# - Pedido #4: Token=token2, Monto=$500
# - Pedido #5: Token=token2, Monto=$500
# - Pedido #6: Token=token2, Monto=$500

# H Pylint verifica con "Your code has been rated at 9.29/10" 
