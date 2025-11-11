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