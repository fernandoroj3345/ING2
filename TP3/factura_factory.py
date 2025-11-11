# factura_factory.py

from abc import ABC, abstractmethod

# Clase abstracta
class Factura(ABC):
    def __init__(self, importe):
        self.importe = importe

    @abstractmethod
    def mostrar(self):
        pass


# Subclases concretas
class FacturaA(Factura):
    def mostrar(self):
        print("Factura A - IVA Responsable Inscripto")
        print(f"Importe total: ${self.importe:.2f}")

class FacturaB(Factura):
    def mostrar(self):
        print("Factura B - IVA No Inscripto")
        print(f"Importe total: ${self.importe:.2f}")

class FacturaC(Factura):
    def mostrar(self):
        print("Factura C - IVA Exento")
        print(f"Importe total: ${self.importe:.2f}")


# Fábrica
class FacturaFactory:
    @staticmethod
    def crear_factura(condicion_iva, importe):
        condicion = condicion_iva.strip().upper()
        if condicion == "IVA RESPONSABLE":
            return FacturaA(importe)
        elif condicion == "IVA NO INSCRIPTO":
            return FacturaB(importe)
        elif condicion == "IVA EXENTO":
            return FacturaC(importe)
        else:
            raise ValueError("Condición impositiva no reconocida")


