#Implemento el patrón Flyweight
class ProductoFlyweight:
    """Almacena el estado intrínseco (compartido) de los productos"""
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def mostrar_detalle(self, serial):
        return f"{self.nombre} ({self.categoria}) | Serial: {serial}"

class FabricaFlyweight:
    """Factory para gestionar y reutilizar flyweights"""
    _flyweights = {}

    @classmethod
    def obtener_flyweight(cls, nombre, categoria):
        clave = (nombre.lower(), categoria.lower())  # Normalización
        if clave not in cls._flyweights:
            cls._flyweights[clave] = ProductoFlyweight(nombre, categoria)
        return cls._flyweights[clave]

    @classmethod
    def total_flyweights(cls):
        return len(cls._flyweights)

class ItemInventario:
    """Representa un ítem único con estado extrínseco"""
    def __init__(self, serial, stock, nombre, categoria):
        self.serial = serial
        self.stock = stock
        self.flyweight = FabricaFlyweight.obtener_flyweight(nombre, categoria)

    def detalle_completo(self):
        return f"{self.flyweight.mostrar_detalle(self.serial)} | Stock: {self.stock}"

# === Ejemplo de uso ===
if __name__ == "__main__":
    # Creación de ítems
    items = [
        ItemInventario("SN001", 50, "Teclado Gamer", "Periféricos"),
        ItemInventario("SN002", 30, "Teclado Gamer", "Periféricos"),
        ItemInventario("SN003", 100, "Mouse RGB", "Periféricos"),
        ItemInventario("SN004", 20, "Monitor 24'", "Pantallas"),
        ItemInventario("SN005", 15, "Monitor 24'", "Pantallas")
    ]

    # Mostrar detalles
    print("=== Detalles de inventario ===")
    for item in items:
        print(item.detalle_completo())

    # Verificación de optimización
    print("\n=== Estadísticas de Flyweights ===")
    print(f"Total de ítems creados: {len(items)}")
    print(f"Total de flyweights en memoria: {FabricaFlyweight.total_flyweights()}")
    print(f"Memoria optimizada: {round((1 - FabricaFlyweight.total_flyweights()/len(items)) * 100, 2)}%")

    # Demostración de compartir estado
    print("\n=== Verificación de flyweights compartidos ===")
    print("Mismo flyweight para teclados:", items[0].flyweight is items[1].flyweight)  # True
    print("Mismo flyweight para monitores:", items[3].flyweight is items[4].flyweight)  # True
    print("Flyweight diferente entre teclado y mouse:", items[0].flyweight is items[2].flyweight)  # False
