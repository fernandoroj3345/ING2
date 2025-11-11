from abc import ABC, abstractmethod

# Sujeto (Observable)
class EmisorID:
    def __init__(self):
        self._observadores = []

    def suscribir(self, observador):
        self._observadores.append(observador)

    def desuscribir(self, observador):
        self._observadores.remove(observador)

    def emitir_id(self, id_emitido):
        print(f"\nEmisor: Emitiendo ID '{id_emitido}'")
        for obs in self._observadores:
            obs.actualizar(id_emitido)

# Observador base
class Observador(ABC):
    def __init__(self, id_propio):
        self.id_propio = id_propio

    @abstractmethod
    def actualizar(self, id_emitido):
        pass

# Observadores concretos
class ObservadorA(Observador):
    def actualizar(self, id_emitido):
        if id_emitido == self.id_propio:
            print(f"ObservadorA: ¡ID coincidente '{self.id_propio}' recibido!")

class ObservadorB(Observador):
    def actualizar(self, id_emitido):
        if id_emitido == self.id_propio:
            print(f"ObservadorB: ¡ID coincidente '{self.id_propio}' recibido!")

class ObservadorC(Observador):
    def actualizar(self, id_emitido):
        if id_emitido == self.id_propio:
            print(f"ObservadorC: ¡ID coincidente '{self.id_propio}' recibido!")

class ObservadorD(Observador):
    def actualizar(self, id_emitido):
        if id_emitido == self.id_propio:
            print(f"ObservadorD: ¡ID coincidente '{self.id_propio}' recibido!")

# Uso
if __name__ == "__main__":
    emisor = EmisorID()

    # Crear observadores con IDs propios
    obs_a = ObservadorA("AB12")
    obs_b = ObservadorB("CD34")
    obs_c = ObservadorC("EF56")
    obs_d = ObservadorD("GH78")

    # Suscribir observadores al emisor
    emisor.suscribir(obs_a)
    emisor.suscribir(obs_b)
    emisor.suscribir(obs_c)
    emisor.suscribir(obs_d)

    # IDs a emitir (8 en total, 4 coinciden con IDs de observadores)
    ids_emitidos = ["XY99", "AB12", "ZZ00", "CD34", "EF56", "MNOP", "GH78", "1234"]

    for id_ in ids_emitidos:
        emisor.emitir_id(id_)

"""
EmisorID mantiene una lista de observadores y les notifica cada vez que emite un ID.

Cada observador tiene un ID propio y solo emite un mensaje cuando el ID emitido coincide con el suyo.

Se crean cuatro observadores con IDs "AB12", "CD34", "EF56" y "GH78".

Se emiten 8 IDs, de los cuales 4 coinciden con los IDs de los observadores.


"""