class CuentaHandler:
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler  # permite encadenar

    def procesar_pago(self, monto):
        raise NotImplementedError("Este método debe ser implementado por subclases")


class CuentaConcreteHandler(CuentaHandler):
    def __init__(self, nombre, saldo):
        super().__init__()
        self.nombre = nombre
        self.saldo = saldo

    def procesar_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Pago de ${monto:.2f} procesado desde: {self.nombre}")
            print(f"Saldo restante en {self.nombre}: ${self.saldo:.2f}")
        elif self._next:
            print(f"Saldo insuficiente en {self.nombre}. Probando siguiente cuenta...")
            self._next.procesar_pago(monto)
        else:
            print(f"Pago de ${monto:.2f} no pudo ser procesado. Fondos insuficientes en todas las cuentas.")


# ---------------------
#  Cadena de comando
# ---------------------
if __name__ == "__main__":
    # Crear cuentas
    cuenta1 = CuentaConcreteHandler("token1", 1000)
    cuenta2 = CuentaConcreteHandler("token2", 2000)

    # Configurar la cadena: token1 -> token2
    cuenta1.set_next(cuenta2)

    # Casos de prueba
    cuenta1.procesar_pago(800)   # Debe usar token1
    cuenta1.procesar_pago(500)   # Debe usar token2 (ya no alcanza en token1)
    cuenta1.procesar_pago(3000)  # Ninguna puede procesar


