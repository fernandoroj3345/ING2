# factorial_singleton.py

class FactorialSingleton:
    _instancia = None  # Variable de clase que guarda la única instancia

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(FactorialSingleton, cls).__new__(cls)
        return cls._instancia

    def calcular(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("El número debe ser un entero no negativo")
        return 1 if n == 0 else n * self.calcular(n - 1)


# Ejemplo de uso
if __name__ == "__main__":
    f1 = FactorialSingleton()
    f2 = FactorialSingleton()

    print(f"Factorial de 5: {f1.calcular(5)}")
    print(f"¿f1 y f2 son la misma instancia? {'Sí' if f1 is f2 else 'No'}")


       

#FactorialSingleton asegura que solo exista una instancia gracias al método  __new__.
#La función calcular implementa el cálculo del factorial de forma recursiva.
#Si intento crear múltiples objetos, todos serán en realidad la misma instancia.
