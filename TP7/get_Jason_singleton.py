import json
import sys

class JsonInspectorSingleton:
    _instance = None  # Variable de clase para guardar la única instancia

    def __new__(cls, filepath):
        if cls._instance is None:
            cls._instance = super(JsonInspectorSingleton, cls).__new__(cls)
            cls._instance._initialized = False  # Bandera para evitar reinit
        return cls._instance

    def __init__(self, filepath):
        if not self._initialized:
            self.filepath = filepath
            self.data = None
            self._initialized = True  # Marcar como inicializado

    def load(self):
        try:
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"Error: El archivo '{self.filepath}' no existe.")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error: El archivo no contiene un JSON válido.")
            sys.exit(1)

    def inspect_keys(self, keys):
        if self.data is None:
            print("Error: Los datos no han sido cargados.")
            return
        
        for key in keys:
            value = self.data.get(key)
            if value is not None:
                print(f"{key}: {value}")
            else:
                print(f"{key} no encontrado en el archivo JSON")

# Ejecución desde línea de comandos
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py archivo.json")
        sys.exit(1)

    archivo_json = sys.argv[1]
    claves = ['token1', 'token2']

    inspector = JsonInspectorSingleton(archivo_json)
    inspector.load()
    inspector.inspect_keys(claves)
