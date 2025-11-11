#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*


##########################################
import sys

class Factorial:
    def init(self):
        pass

    def factorial(self, num):
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

    def run(self, min_val, max_val):
        print(f"Factorial de {min_val} es {self.factorial(min_val)}")
        print(f"Factorial de {max_val} es {self.factorial(max_val)}")

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

factorial_calculadora = Factorial()
factorial_calculadora.run(inicio, fin)