from abc import ABC, abstractmethod

# Clase base abstracta para los manejadores
class Manejador(ABC):
    def __init__(self):
        self.siguiente = None

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def manejar(self, numero):
        if self.puede_manejar(numero):
            self.consumir(numero)
        elif self.siguiente:
            self.siguiente.manejar(numero)
        else:
            print(f"Número {numero} no consumido")

    @abstractmethod
    def puede_manejar(self, numero):
        pass

    @abstractmethod
    def consumir(self, numero):
        pass

# Manejador para números primos
class ManejadorPrimos(Manejador):
    def puede_manejar(self, numero):
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def consumir(self, numero):
        print(f"Número primo consumido: {numero}")

# Manejador para números pares
class ManejadorPares(Manejador):
    def puede_manejar(self, numero):
        return numero % 2 == 0

    def consumir(self, numero):
        print(f"Número par consumido: {numero}")

# Uso de la cadena de responsabilidad
if __name__ == "__main__":
    # Crear manejadores
    primo = ManejadorPrimos()
    par = ManejadorPares()

    # Configurar cadena: primo -> par
    primo.set_siguiente(par)

    # Procesar números del 1 al 100
    for num in range(1, 101):
        primo.manejar(num)


"""
La clase abstracta Manejador define la interfaz común y la lógica para pasar la responsabilidad 
al siguiente manejador si el actual no puede consumir el número.

ManejadorPrimos verifica si un número es primo y lo consume si es así.

ManejadorPares verifica si un número es par y lo consume si es así.

Si ningún manejador consume el número, se imprime que no fue consumido.

La cadena está configurada para que el manejador de primos intente primero, y si no consume, pasa al
manejador de pares
"""