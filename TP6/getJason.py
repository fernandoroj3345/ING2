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
#Modificacion del getJason.py es el punto (2F)
import json
import sys

jsonfile = sys.argv[1]       # Toma el nombre del archivo JSON desde la línea de comandos
jsonkeys = ['token1', 'token2']  # Lista de claves a buscar

# Abro y lee el archivo JSON
with open(jsonfile, 'r') as myfile:
    data = myfile.read()

# Parsea el contenido como objeto JSON (diccionario)
obj = json.loads(data)

# Recorre cada clave y muestra su valor
for key in jsonkeys:
    if key in obj:
        print(f"{key}: {obj[key]}")
    else:
        print(f"{key} no encontrado en el archivo JSON")

