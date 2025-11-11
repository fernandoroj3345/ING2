def collatz(num):
    if not (1 <= num <= 1999):
        raise ValueError("Número fuera del rango permitido")
    iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones

# Test cases

def test_collatz():
    # Test unitarios (caja blanca)
    assert collatz(1) == 0, "T1 Falló: 1 debe retornar 0 iteraciones"
    assert collatz(2) == 1, "T2 Falló: 2 debe retornar 1 iteración"
    assert collatz(3) == 7, "T3 Falló: 3 debe retornar 7 iteraciones"
    assert collatz(27) == 111, "T4 Falló: 27 debe retornar 111 iteraciones"

    # Test funcionales (caja negra) - pruebas de validación
    # Como la función collatz no valida directamente la entrada,
    # simulamos manejo externo:
    try:
        collatz(0)
        print("T5 Falló: debe manejar entrada inválida 0")
    except Exception:
        print("T5 Pasó: entrada inválida 0 manejada")

    try:
        collatz(2000)
        print("T6 Falló: debe manejar entrada inválida 2000")
    except Exception:
        print("T6 Pasó: entrada inválida 2000 manejada")


if __name__ == "__main__":
    # Prueba los tests
    test_collatz()
    print("Pruebas finalizadas.")
