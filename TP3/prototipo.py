# prototipo.py

import copy

class Prototipo:
    def clonar(self):
        # Devuelve una copia profunda de sí mismo
        return copy.deepcopy(self)


# Subclase concreta
class Documento(Prototipo):
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def mostrar(self):
        print(f"Título: {self.titulo}\nContenido: {self.contenido}")


# Ejemplo de uso
if __name__ == "__main__":
    doc_original = Documento("Informe F1", "Esto es lo original.")
    doc_original.mostrar()

    print("\n🌀 Clonando documento original...")
    doc_clon1 = doc_original.clonar()
    doc_clon1.titulo = "Informe F1 (copia 1)"
    doc_clon1.mostrar()

    print("\n🔁 Clonando el clon...")
    doc_clon2 = doc_clon1.clonar()
    doc_clon2.titulo = "Informe F1 (copia 2)"
    doc_clon2.mostrar()

#Prototipo define el método clonar() usando copy.deepcopy() para asegurar una copia completa.

#Documento hereda de Prototipo, por lo que puede clonarse a sí mismo.

#Tanto el objeto original como sus copias pueden seguir clonándose indefinidamente.