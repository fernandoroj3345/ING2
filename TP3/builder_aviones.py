# builder_aviones.py

from abc import ABC, abstractmethod

# Producto
class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def especificaciones(self):
        return f"Partes del avión: {', '.join(self.partes)}"


# Builder abstracto
class BuilderAvion(ABC):
    def __init__(self):
        self.avion = Avion()

    @abstractmethod
    def construir_body(self):
        pass

    @abstractmethod
    def construir_turbinas(self):
        pass

    @abstractmethod
    def construir_alas(self):
        pass

    @abstractmethod
    def construir_tren_aterrizaje(self):
        pass

    def obtener_avion(self):
        return self.avion


# Concrete Builder
class BuilderAvionComercial(BuilderAvion):
    def construir_body(self):
        self.avion.agregar_parte("Body de avión comercial")

    def construir_turbinas(self):
        self.avion.agregar_parte("Turbina izquierda")
        self.avion.agregar_parte("Turbina derecha")

    def construir_alas(self):
        self.avion.agregar_parte("Ala izquierda")
        self.avion.agregar_parte("Ala derecha")

    def construir_tren_aterrizaje(self):
        self.avion.agregar_parte("Tren de aterrizaje principal")


# Director
class DirectorMontajeAvion:
    def __init__(self, builder):
        self.builder = builder

    def construir_avion_completo(self):
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren_aterrizaje()
        return self.builder.obtener_avion()


# Ejemplo de uso
if __name__ == "__main__":
    director = DirectorMontajeAvion(BuilderAvionComercial())
    avion = director.construir_avion_completo()
    print(avion.especificaciones())
