def collatz(num):
    iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones

# Solicitar número al usuario validando entrada y rango
while True:
    try:
        n = int(input("Ingrese un número entero positivo entre 1 y 1999: "))
        if 1 <= n <= 1999:
            break
        else:
            print("Error: El número debe estar entre 1 y 1999.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# Calcular y mostrar el número de iteraciones para alcanzar 1
resultado = collatz(n)
print("El número de iteraciones para %d es %d" % (n, resultado))
