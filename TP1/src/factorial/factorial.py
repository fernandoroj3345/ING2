#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
"""
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 
if len(sys.argv) < 2:
    # Si no se pasó un número, solicita al usuario
    num = int(input("Debe informar un número! Ingrese un número: "))
else:
    # Si se pasó un número como argumento
    num = int(sys.argv[1])

print("Factorial", num, "! es", factorial(num))
"""
##############################################################################
"""
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

#Función para validar y procesar el rango
def procesar_rango(rango):
    try:
        inicio, fin = map(int, rango.split('-'))
        return inicio, fin
    except ValueError:
        print("Formato incorrecto. Debe ser 'inicio-fin' con números enteros.")
        sys.exit()

#Verificar si se pasó un argumento desde la línea de comandos
if len(sys.argv) < 2:
    # Si no se pasó un número, solicita un rango al usuario
    rango = input("Debe informar un rango! Ingrese un rango de la forma inicio-fin: ")
else:
    # Si se pasó un número como argumento
    rango = sys.argv[1]

#Procesar el rango
inicio, fin = procesar_rango(rango)

#Calcular y mostrar el factorial de los extremos
print(f"Factorial de {inicio} es {factorial(inicio)}")
print(f"Factorial de {fin} es {factorial(fin)}")
"""
##########################################

import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def procesar_rango(rango):
    if rango.startswith('-'):
        try:
            fin = int(rango[1:])
            return 1, fin
        except ValueError:
            print("Formato incorrecto para '-hasta'. Debe ser '-número'.")
            sys.exit()
    elif rango.endswith('-'):
        try:
            inicio = int(rango[:-1])
            return inicio, 60
        except ValueError:
            print("Formato incorrecto para 'desde-'. Debe ser 'número-'.")
            sys.exit()
    else:
        try:
            inicio, fin = map(int, rango.split('-'))
            return inicio, fin
        except ValueError:
            print("Formato incorrecto. Debe ser 'inicio-fin' o '-hasta' o 'desde-'.")
            sys.exit()

if len(sys.argv) < 2:
    rango = input("Debe informar un rango! Ingrese un rango de la forma inicio-fin, -hasta o desde-: ")
else:
    rango = sys.argv[1]

inicio, fin = procesar_rango(rango)

print(f"Factorial de {inicio} es {factorial(inicio)}")
print(f"Factorial de {fin} es {factorial(fin)}")