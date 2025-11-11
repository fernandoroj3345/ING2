from abc import ABC, abstractmethod

# Componente abstracto
class ComponenteEnsamblado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar(self, nivel=0):
        pass

    @abstractmethod
    def agregar(self, componente):
        pass

    @abstractmethod
    def eliminar(self, componente):
        pass

    @abstractmethod
    def obtener_hijos(self):
        pass

# Hoja (leaf) - representa una pieza individual
class Pieza(ComponenteEnsamblado):
    def mostrar(self, nivel=0):
        print(f"{'  ' * nivel}- Pieza: {self.nombre}")

    def agregar(self, componente):
        raise NotImplementedError("Las piezas no pueden contener otros componentes.")

    def eliminar(self, componente):
        raise NotImplementedError("Las piezas no pueden contener otros componentes.")

    def obtener_hijos(self):
        return []

# Composite - representa un sub-conjunto o el producto principal
class SubConjunto(ComponenteEnsamblado):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.hijos = []

    def agregar(self, componente):
        self.hijos.append(componente)

    def eliminar(self, componente):
        self.hijos.remove(componente)

    def obtener_hijos(self):
        return self.hijos

    def mostrar(self, nivel=0):
        print(f"{'  ' * nivel}+ Sub-conjunto: {self.nombre}")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)

# Clase para el producto principal
class ProductoPrincipal(SubConjunto):
    def __init__(self, nombre):
        super().__init__(nombre)
        print(f"\n--- {nombre} ---")

# Ejemplo de creación y visualización de la configuración inicial
print("--- Configuración Inicial ---")
producto = ProductoPrincipal("Producto Principal")

subconjunto1 = SubConjunto("Sub-conjunto A")
for i in range(1, 5):
    subconjunto1.agregar(Pieza(f"Pieza A{i}"))
producto.agregar(subconjunto1)

subconjunto2 = SubConjunto("Sub-conjunto B")
for i in range(1, 5):
    subconjunto2.agregar(Pieza(f"Pieza B{i}"))
producto.agregar(subconjunto2)

subconjunto3 = SubConjunto("Sub-conjunto C")
for i in range(1, 5):
    subconjunto3.agregar(Pieza(f"Pieza C{i}"))
producto.agregar(subconjunto3)

producto.mostrar()

# Agregando un subconjunto opcional
print("\n--- Agregando Sub-conjunto Opcional ---")
subconjunto_opcional = SubConjunto("Sub-conjunto Opcional")
for i in range(1, 5):
    subconjunto_opcional.agregar(Pieza(f"Pieza O{i}"))
producto.agregar(subconjunto_opcional)

producto.mostrar()

"""
Desglose de las clases y el patrón Composite:

ComponenteEnsamblado (Component):

Es una clase abstracta que define la interfaz común para todos los componentes del ensamblado,
tanto las piezas individuales (hojas) como los sub-conjuntos (composites).
Define los métodos abstractos mostrar(), agregar(), eliminar() y obtener_hijos().
Pieza (Leaf):

Representa un objeto individual, una pieza que no puede contener otros componentes.
Implementa el método mostrar() para mostrar su nombre con la indentación adecuada para indicar su nivel en 
la jerarquía.
Los métodos agregar() y eliminar() lanzan una excepción NotImplementedError porque una pieza no puede
tener hijos.
obtener_hijos() devuelve una lista vacía.
SubConjunto (Composite):

Representa un objeto que puede contener otros componentes, ya sean piezas individuales 
u otros sub-conjuntos.
Mantiene una lista de sus hijos.
Implementa los métodos agregar() y eliminar() para gestionar sus componentes hijos.
El método obtener_hijos() devuelve la lista de sus componentes hijos.
El método mostrar() muestra su propio nombre y luego itera a través de sus hijos, llamando al método
mostrar() de cada hijo con un nivel de indentación aumentado para representar la jerarquía.
ProductoPrincipal:

Es una especialización de SubConjunto que representa el nivel superior del ensamblado. 
Simplemente hereda la funcionalidad de SubConjunto.
Cómo se aplica el patrón Composite:

El patrón Composite se aplica al definir una estructura de árbol donde tanto los objetos
individuales (Pieza) como las composiciones de objetos (SubConjunto, ProductoPrincipal) implementan
la misma interfaz (ComponenteEnsamblado). Esto permite tratar todos los objetos de la estructura de
manera uniforme.

En el ejemplo:

Tanto una Pieza como un SubConjunto tienen el método mostrar(). Podemos llamar a mostrar() en cualquier
objeto de la estructura sin tener que saber si es una pieza individual o un conjunto de piezas.
Un SubConjunto puede contener otras Piezas o incluso otros SubConjuntos, creando así la jerarquía.
Beneficios del patrón Composite:

Uniformidad: Permite tratar objetos individuales y composiciones de objetos de la misma manera, simplificando
el código del cliente.
Simplicidad: Facilita la manipulación de estructuras complejas, ya que las operaciones se pueden aplicar
de manera recursiva a toda la estructura.
Extensibilidad: Es fácil agregar nuevos tipos de componentes (tanto hojas como composites) sin modificar 
el código del cliente que utiliza la interfaz común.
Organización: Clarifica la estructura jerárquica de un sistema.
En resumen, el patrón Composite nos permite construir estructuras de objetos jerárquicas y tratarlas 
de manera uniforme, lo cual es muy útil para representar ensamblados, estructuras de directorios, 
interfaces de usuario, etc
"""