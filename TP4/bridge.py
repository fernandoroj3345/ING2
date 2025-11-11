from abc import ABC, abstractmethod

# Interfaz para los trenes laminadores (la "implementación")
class TrenLaminador(ABC):
    @abstractmethod
    def producir_lamina(self, espesor, ancho, largo):
        pass

# Implementaciones concretas de los trenes laminadores
class TrenLaminadorCorto(TrenLaminador):
    def producir_lamina(self, espesor, ancho, largo):
        if largo <= 5:
            print(f"Tren Laminador Corto: Produciendo lámina de {espesor}\" de espesor, {ancho} metros de ancho y {largo} metros de largo.")
        else:
            print(f"Tren Laminador Corto: No puede producir láminas de {largo} metros de largo. Longitud máxima: 5 metros.")

class TrenLaminadorLargo(TrenLaminador):
    def producir_lamina(self, espesor, ancho, largo):
        if largo <= 10:
            print(f"Tren Laminador Largo: Produciendo lámina de {espesor}\" de espesor, {ancho} metros de ancho y {largo} metros de largo.")
        else:
            print(f"Tren Laminador Largo: No puede producir láminas de {largo} metros de largo. Longitud máxima: 10 metros.")

# Abstracción para la lámina de acero
class LaminaAcero:
    def __init__(self, espesor, ancho, tren_laminador: TrenLaminador):
        self.espesor = espesor
        self.ancho = ancho
        self.tren_laminador = tren_laminador

    def producir(self, largo):
        self.tren_laminador.producir_lamina(self.espesor, self.ancho, largo)

# Abstracciones refinadas (opcional, para especializar aún más las láminas)
class LaminaAceroEstándar(LaminaAcero):
    def __init__(self, tren_laminador: TrenLaminador):
        super().__init__(0.5, 1.5, tren_laminador)

class LaminaAceroAnchoEspecial(LaminaAcero):
    def __init__(self, ancho, tren_laminador: TrenLaminador):
        super().__init__(0.5, ancho, tren_laminador)

# Ejemplo de uso
if __name__ == "__main__":
    tren_corto = TrenLaminadorCorto()
    tren_largo = TrenLaminadorLargo()

    lamina1 = LaminaAceroEstándar(tren_corto)
    lamina1.producir(4)
    lamina1.producir(6)

    lamina2 = LaminaAceroEstándar(tren_largo)
    lamina2.producir(8)
    lamina2.producir(12)

    lamina_ancho_especial = LaminaAceroAnchoEspecial(2.0, tren_largo)
    lamina_ancho_especial.producir(9)


    """
    Desglose de la solución y el patrón Bridge:

Interfaz TrenLaminador (la "Implementación"):

Define la interfaz para las clases de trenes laminadores concretos. En este caso, tiene un único método
abstracto producir_lamina que toma el espesor, ancho y largo de la lámina como argumentos.
Implementaciones Concretas (TrenLaminadorCorto, TrenLaminadorLargo):

Estas clases implementan la interfaz TrenLaminador y proporcionan la lógica específica para cada tipo de tren.
TrenLaminadorCorto puede producir láminas de hasta 5 metros de largo.
TrenLaminadorLargo puede producir láminas de hasta 10 metros de largo.
Cada implementación incluye una validación básica del largo de la lámina que puede producir.
Abstracción LaminaAcero (la "Abstracción"):

Esta es la clase genérica que representa una lámina de acero.
Contiene atributos para el espesor y el ancho (que son fijos para el producto específico).
Lo crucial aquí es que recibe una instancia de un TrenLaminador en su constructor.
Esta es la conexión (el "puente") con la implementación.
El método producir delega la responsabilidad de la producción real al objeto TrenLaminador asociado.
Abstracciones Refinadas (Opcional):

Las clases LaminaAceroEstándar y LaminaAceroAnchoEspecial son ejemplos de cómo se puede extender
la abstracción LaminaAcero para crear variantes más específicas del producto, manteniendo
la flexibilidad de elegir la implementación del tren laminador.
LaminaAceroEstándar crea una lámina con el espesor y ancho especificados en el problema.
LaminaAceroAnchoEspecial permite crear láminas con un ancho diferente, manteniendo el espesor estándar.
Cómo se aplica el patrón Bridge:

El patrón Bridge se aplica al separar la clase LaminaAcero (la abstracción) de las clases concretas de 
TrenLaminador (las implementaciones). En lugar de tener una jerarquía de clases LaminaAceroCorto,
LaminaAceroLargo, etc., la clase LaminaAcero se asocia con un objeto TrenLaminador a través de la composición.

Beneficios del patrón Bridge en este caso:

Desacoplamiento: La clase LaminaAcero no está ligada a una implementación específica de un tren laminador. 
Podemos agregar nuevos tipos de trenes laminadores sin modificar la clase LaminaAcero o sus abstracciones 
refinadas.
Flexibilidad: Podemos decidir en tiempo de ejecución qué tren laminador se utilizará para producir una lámina 
en particular.
Extensibilidad: Podemos extender tanto la abstracción (creando nuevas especializaciones de láminas)
como la implementación (creando nuevos tipos de trenes laminadores) de forma independiente.
Mejor organización: Separa claramente la lógica de la lámina de acero de la lógica de los diferentes 
procesos de laminado.
En resumen, al utilizar el patrón Bridge, hemos creado una representación flexible y extensible para 
la producción de láminas de acero, donde la lógica del producto (la lámina) está separada de las diferentes
maneras en que se puede fabricar (los trenes laminadores).
    """