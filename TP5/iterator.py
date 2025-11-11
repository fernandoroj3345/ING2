class IteradorCadena:
    def __init__(self, cadena):
        self._cadena = cadena
        self._indice = 0

    def __iter__(self):
        self._indice = 0  # Reiniciar índice para iteración directa
        return self

    def __next__(self):
        if self._indice < len(self._cadena):
            caracter = self._cadena[self._indice]
            self._indice += 1
            return caracter
        else:
            raise StopIteration

    def iter_reverso(self):
        self._indice = len(self._cadena) - 1  # Empezar desde el final
        return self

    def siguiente_reverso(self):
        if self._indice >= 0:
            caracter = self._cadena[self._indice]
            self._indice -= 1
            return caracter
        else:
            raise StopIteration


# Ejemplo de uso
if __name__ == "__main__":
    texto = IteradorCadena("Hola Mundo")

    print("Iteración directa:")
    for c in texto:
        print(c, end=' ')
    print()

    print("Iteración inversa:")
    iter_rev = texto.iter_reverso()
    try:
        while True:
            c = iter_rev.siguiente_reverso()
            print(c, end=' ')
    except StopIteration:
        pass


"""
La clase IteradorCadena almacena la cadena y un índice interno.

Implementa los métodos __iter__ y __next__ para permitir iterar en sentido directo con un for.

Para la iteración inversa, se usa el método iter_reverso que prepara el índice para recorrer 
desde el final, y siguiente_reverso que devuelve el siguiente carácter hacia atrás.

En el ejemplo, se muestra cómo recorrer la cadena "Hola Mundo" primero de forma directa y luego en reverso.
"""