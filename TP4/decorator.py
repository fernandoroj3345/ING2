#Implementación del patrón Decorator
#Clase Base (Numero)
#Define el objeto central que almacena el valor numérico:

class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        return self.valor

#Clase Decoradora Base (DecoradorBase)
#Actúa como interfaz común para todos los decoradores:

class DecoradorBase:
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        return self.numero.imprimir()

#Decoradores Concretos
#Añaden funcionalidades matemáticas en cascada:

class SumarDos(DecoradorBase):
    def imprimir(self):
        return self.numero.imprimir() + 2

class MultiplicarPorDos(DecoradorBase):
    def imprimir(self):
        return self.numero.imprimir() * 2

class DividirPorTres(DecoradorBase):
    def imprimir(self):
        return self.numero.imprimir() / 3

#Resultados de operaciones
#Sin decoradores
#El objeto base devuelve su valor original:
num = Numero(10)
print(num.imprimir())  # 10 [1][2]


#con decorador anidados
#Los decoradores se aplican en secuencia (suma → multiplicación → división):
num_decorado = DividirPorTres(MultiplicarPorDos(SumarDos(num)))
print(num_decorado.imprimir())  # 8.0 [1][2]
