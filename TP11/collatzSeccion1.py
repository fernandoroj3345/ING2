#código de las pruebas (collatzTest.py) corregido, asumiendo que tu función collatz(n) debe devolver el número de pasos que tarda
#la secuencia en llegar a 1.

#He modificado el test T1 para que pruebe el número 5, que era el que causaba el fallo, aunque en la salida el nombre del test era
# test_T1_numero_1.
#Asumiendo que pruebo con 5 ya que la aserción era collatz(5).

import unittest

# ************************************************
# NOTA: Debes asegurarte de que tu función collatz
#       esté definida en algún lugar (o importada).
#       Asumimos que está aquí o en otro archivo.
# ************************************************

# Función collatz (ejemplo de cómo podría ser, si no la tienes)
def collatz(n):
    # Caso especial (puede variar según la definición)
    if n <= 0:
        return 0 
    
    steps = 0
    current_n = n
    while current_n != 1: # 1. El ciclo se detiene en 1
        if current_n % 2 == 0:
            current_n = current_n / 2
        else:
            current_n = 3 * current_n + 1
        steps += 1 # 2. El contador se incrementa dentro del ciclo
    return steps

class TestCollatz(unittest.TestCase):
    #...
    # 1. Test para n=5 (Requiere 5 pasos: 5 -> 16 -> 8 -> 4 -> 2 -> 1)
    def test_collatz_para_el_numero_5(self):
        """Verifico que collatz(5) devuelve 5 pasos."""
        self.assertEqual(collatz(5), 5)

    # 2. Test para n=56 (Requiere 19 pasos)
    def test_collatz_para_el_numero_56(self):
        # Corrección: El valor esperado es 19, no 1
        self.assertEqual(collatz(56), 19)

    # 3. Test para n=3 (Requiere 7 pasos: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1)
    def test_collatz_para_el_numero_3(self):
        # Este test pasó originalmente
        self.assertEqual(collatz(3), 7)
        
    # 4. Test para n=78 (Requiere 35 pasos)
    def test_collatz_para_el_numero_78(self):
        # Corrección: El valor esperado es 35, no 111
        self.assertEqual(collatz(78), 35)

    # 5. Test para n=0 (Asumiendo 0 pasos o un manejo de error)
    def test_collatz_para_el_numero_0(self):
        # Este test pasó originalmente, asumiendo que collatz(0) devuelve 0
        self.assertEqual(collatz(0), 0)

    # 6. Test para n=2000 (Requiere 111 pasos)
    def test_collatz_para_el_numero_2000(self):
        # Este test pasó originalmente
        self.assertEqual(collatz(2000), 112)

if __name__ == '__main__':
    unittest.main()

