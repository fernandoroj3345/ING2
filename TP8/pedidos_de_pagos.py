class CuentaHandler:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def puede_procesar(self, monto):
        return self.saldo >= monto

    def procesar_pago(self, monto):
        self.saldo -= monto
        return self.nombre


class Pago:
    def __init__(self, numero, token, monto):
        self.numero = numero
        self.token = token
        self.monto = monto

    def __str__(self):
        return f"Pedido #{self.numero}: Token={self.token}, Monto=${self.monto}"


class RegistroPagos:
    def __init__(self):
        self._pagos = []

    def agregar_pago(self, pago):
        self._pagos.append(pago)

    def __iter__(self):
        return iter(self._pagos)


class PagoManager:
    def __init__(self):
        self.cuentas = [
            CuentaHandler("token1", 1000),
            CuentaHandler("token2", 2000)
        ]
        self.registro = RegistroPagos()
        self.turno = 0  # Alternar entre 0 y 1

    def procesar_pedido(self, numero_pedido, monto):
        intentos = 0
        for _ in range(len(self.cuentas)):
            cuenta = self.cuentas[self.turno]
            if cuenta.puede_procesar(monto):
                cuenta.procesar_pago(monto)
                pago = Pago(numero_pedido, cuenta.nombre, monto)
                self.registro.agregar_pago(pago)
                print(str(pago))
                self.turno = (self.turno + 1) % len(self.cuentas)
                return
            else:
                # Cambiar de cuenta e intentar la otra
                self.turno = (self.turno + 1) % len(self.cuentas)
                intentos += 1

        print(f"Pedido #{numero_pedido}: No hay cuentas con saldo suficiente para ${monto}")

    def listar_pagos(self):
        print("\n Listado de pagos:")
        for pago in self.registro:
            print(f" - {pago}")


if __name__ == "__main__":
    gestor = PagoManager()

    # Procesar varios pagos de $500 con número de pedido
    for i in range(1, 8):
        gestor.procesar_pedido(i, 500)

    gestor.listar_pagos()
