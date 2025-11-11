# inventario_factory.py

from abc import ABC, abstractmethod

# === Producto base ===
class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def mostrar(self):
        pass

# === Productos concretos ===
class Televisor(Producto):
    def mostrar(self):
        print(f"📺 {self.nombre} - ${self.precio}")

class Computadora(Producto):
    def mostrar(self):
        print(f"💻 {self.nombre} - ${self.precio}")

class Pan(Producto):
    def mostrar(self):
        print(f"🍞 {self.nombre} - ${self.precio}")

class Queso(Producto):
    def mostrar(self):
        print(f"🧀 {self.nombre} - ${self.precio}")

class Camisa(Producto):
    def mostrar(self):
        print(f"👕 {self.nombre} - ${self.precio}")

class Pantalon(Producto):
    def mostrar(self):
        print(f"👖 {self.nombre} - ${self.precio}")

# === Abstract Factory ===
class FamiliaProductoFactory(ABC):
    @abstractmethod
    def crear_producto1(self): pass

    @abstractmethod
    def crear_producto2(self): pass

# === Fábricas concretas ===
class ElectronicaFactory(FamiliaProductoFactory):
    def crear_producto1(self): return Televisor("Smart TV 50\"", 120000)
    def crear_producto2(self): return Computadora("Notebook Ryzen 7", 210000)

class AlimentosFactory(FamiliaProductoFactory):
    def crear_producto1(self): return Pan("Pan casero", 300)
    def crear_producto2(self): return Queso("Queso cheddar", 800)

class RopaFactory(FamiliaProductoFactory):
    def crear_producto1(self): return Camisa("Camisa blanca", 5000)
    def crear_producto2(self): return Pantalon("Pantalón jeans", 7500)

# === Clase Inventario ===
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_familia(self, factory: FamiliaProductoFactory):
        self.productos.append(factory.crear_producto1())
        self.productos.append(factory.crear_producto2())

    def mostrar_inventario(self):
        print("🧾 Inventario actual:")
        for producto in self.productos:
            producto.mostrar()

# === Ejemplo de uso ===
if __name__ == "__main__":
    inventario = Inventario()

    # Agregamos productos de distintas familias (2x cada una)
    inventario.agregar_familia(ElectronicaFactory())
    inventario.agregar_familia(AlimentosFactory())
    inventario.agregar_familia(RopaFactory())
    
    # Duplicamos alimentos y ropa para llegar a 10 productos
    inventario.agregar_familia(AlimentosFactory())
    inventario.agregar_familia(RopaFactory())

    inventario.mostrar_inventario()


#Puedo cambiar fácilmente la familia de productos agregados (por ejemplo, una fábrica JuguetesFactory).

#Permite escalar agregando nuevos tipos de productos sin tocar Inventario.

#Sigue los principios de desacoplamiento y extensibilidad del patrón Abstract Factory