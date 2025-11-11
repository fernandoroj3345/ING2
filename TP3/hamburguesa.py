# hamburguesa.py

class Hamburguesa:
    def __init__(self, nombre="Hamburguesa clásica"):
        self.nombre = nombre

    def entregar_en_mostrador(self):
        print(f"{self.nombre} entregada en mostrador.")

    def retirar_por_cliente(self):
        print(f"{self.nombre} retirada por el cliente.")

    def enviar_por_delivery(self):
        print(f"{self.nombre} enviada por delivery.")


# Ejemplo de uso
if __name__ == "__main__":
    mi_hamburguesa = Hamburguesa("Hamburguesa con queso")

    mi_hamburguesa.entregar_en_mostrador()
    mi_hamburguesa.retirar_por_cliente()
    mi_hamburguesa.enviar_por_delivery()
