#2A) Lo obtenido es el codigo .pyc descompilado con su version y los siguientes datos
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: getJason.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-05-06 19:05:36 UTC (1746558336)
"""
import json
import sys
jsonfile = sys.argv[1]
jsonkey = 'token1'
with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)
print(str(obj[jsonkey]))
"""

#2B Paso 1 Obtuve la coleccion de datos mediante descompilando el archivo getjson.pyc
#Paso 2 atraves de la ejecucion del programa getJson.pyc obtuve la clave token.
#Paso 3 Componentes del Código:
##Módulos usados:
#json: para procesar datos en formato JSON.
#sys: para acceder a argumentos de línea de comandos.
#Variables:
#jsonfile: ruta al archivo JSON (argumento sys.argv[1])
#jsonkey: clave fija "token1"
#data: contenido del archivo leído como texto
#obj: objeto tipo diccionario resultante del json.loads(data)
#3. Estructura de Datos:
#Se espera un archivo JSON con formato de diccionario, por ejemplo:
#json
#Copiar
#Editar
#{
#  "token1": "abc123",
#  "token2": "xyz456"
#}
#4. Proceso Interno (Flujo de ejecución):
#Inicio del script
#Lectura del argumento (nombre del archivo JSON)
#Apertura y lectura del contenido del archivo
#Parseo del contenido a un objeto Python (dict)
#Acceso al valor de la clave "token1"
#Impresión en consola
#Fin del script
#5. Fuentes de Complejidad:
#No pasar el nombre de archivo → IndexError
#Archivo no existente o no accesible → FileNotFoundError
#JSON mal formado → JSONDecodeError
#Clave "token1" no existente en el JSON → KeyError
#No se manejan excepciones ni errores en el script original.

#Paso 4
El script lee un archivo JSON desde línea de comandos, extrae la clave "token1" y muestra su valor. No valida errores (archivo faltante, JSON inválido, clave inexistente). Es lineal, sin funciones ni validaciones. Mejora posible: aceptar cualquier clave y manejar excepciones.

#Paso 5 
Usuario → Script : Ejecuta con archivo.json
Script → SO       : Solicita argumento (sys.argv[1])
Script → Sistema de Archivos : Abre archivo JSON
Sistema de Archivos → Script : Devuelve contenido
Script → json.loads() : Convierte texto a dict
json.loads() → Script : Devuelve diccionario
Script → Diccionario : Accede a clave 'token1'
Diccionario → Script : Devuelve valor
Script → Consola : Imprime valor
┌────────────────────────────┐
│ Inicio del Script          │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Leer argumento sys.argv[1]│
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Abrir archivo JSON         │
│ (jsonfile)                 │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Leer contenido del archivo │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Convertir a dict con JSON  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Buscar clave "token1"      │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Imprimir valor en consola  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Fin del Script             │
└────────────────────────────┘
#Paso 6 
TP6
├── README.md              # Se encuentran todos los puntos del tp6
├── getJason.py            # Código descompilado o reescrito
├── sitedata.json          # Archivo JSON de prueba
├── getJason.pyc           # Codigo compilado
├
│           
│         
└── .git/                  # Carpeta oculta de Git

2C: 
El comportamiento el es siguiente, osea que no se comporta como el 2b
raceback (most recent call last):
  File "/home/fernando/Fernando/Mi-Carpeta/UADER_IS2_RojasF/TP6/getJason.py", line 8, in <module>
    jsonfile = sys.argv[1]
               ~~~~~~~~^^^
IndexError: list index out of range

E: Las razones obtenidas entre el codigo obtenido y la documentacion, es que ambas no 
