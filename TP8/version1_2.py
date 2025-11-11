"""Módulo de gestión de pagos - versión 1.2"""
print("Iniciando versión 1.2")

__version__ = "1.2"

from typing import List, Iterator


SALDO_INICIAL_TOKEN1 = 1000
SALDO_INICIAL_TOKEN2 = 2000
MONTO_POR_PEDIDO = 500


class CuentaHandler:
    """Representa una cuenta bancaria identificada por un token y un saldo."""

    def __init__(self, nombre: str, saldo: float) -> None:
        self.nombre = nombre
        self.saldo = saldo

    def puede_procesar(self, monto: float) -> bool:
        """Verifica si la cuenta tiene saldo suficiente para un pago."""
        return self.saldo >= monto

    def procesar_pago(self, monto: float) -> str:
        """Descuenta el monto del saldo y retorna el nombre del token utilizado."""
        self.saldo -= monto
        return self.nombre


class Pago:
    """Representa un pedido de pago realizado desde una cuenta/token."""

    def __init__(self, numero: int, token: str, monto: float) -> None:
        self.numero = numero
        self.token = token
        self.monto = monto

    def __str__(self) -> str:
        return f"Pedido #{self.numero}: Token={self.token}, Monto=${self.monto}"


class RegistroPagos:
    """Contiene un registro cronológico de todos los pagos realizados."""

    def __init__(self) -> None:
        self._pagos: List[Pago] = []

    def agregar_pago(self, pago: Pago) -> None:
        """Agrega un nuevo pago al registro."""
        self._pagos.append(pago)

    def __iter__(self) -> Iterator[Pago]:
        """Permite iterar sobre los pagos registrados."""
        return iter(self._pagos)


class PagoManager:
    """Gestiona el procesamiento de pagos entre múltiples cuentas."""

    def __init__(self) -> None:
        self.cuentas = [
            CuentaHandler("token1", SALDO_INICIAL_TOKEN1),
            CuentaHandler("token2", SALDO_INICIAL_TOKEN2)
        ]
        self.registro = RegistroPagos()
        self.turno = 0  # Alterna entre cuentas

    def procesar_pedido(self, numero_pedido: int, monto: float) -> None:
        """Procesa un pedido de pago usando la cuenta disponible con saldo suficiente."""
        for _ in range(len(self.cuentas)):
            cuenta = self.cuentas[self.turno]
            if cuenta.puede_procesar(monto):
                cuenta.procesar_pago(monto)
                pago = Pago(numero_pedido, cuenta.nombre, monto)
                self.registro.agregar_pago(pago)
                print(str(pago))
                self.turno = (self.turno + 1) % len(self.cuentas)
                return
            self.turno = (self.turno + 1) % len(self.cuentas)

        print(f"Pedido #{numero_pedido}: No hay cuentas con saldo suficiente para ${monto}")

    def listar_pagos(self) -> None:
        """Imprime el listado cronológico de pagos realizados."""
        print("\n Listado de pagos realizados:")
        for pago in self.registro:
            print(f" - {pago}")


if __name__ == "__main__":
    print("Iniciando versión 1.2") 

    gestor_pagos = PagoManager()

    for i in range(1, 8):
        gestor_pagos.procesar_pedido(i, MONTO_POR_PEDIDO)

    gestor_pagos.listar_pagos()

