def collatz(num):
    iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones

# Solicito número al usuario validando el rango y tipo
while True:
    try:
        n = int(input("Ingrese un número entero positivo (máx 1999): "))
        if 1 <= n <= 1999:
            break
        else:
            print("Error: El número debe estar entre 1 y 1999.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# Calcula iteraciones y muestra resultado
resultado = collatz(n)
print("El número de iteraciones para %d es %d" % (n, resultado))
