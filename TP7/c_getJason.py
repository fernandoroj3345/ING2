import json
import sys
import os

class JsonInspectorSingleton:
    _instance = None

    def __new__(cls, filepath):
        if cls._instance is None:
            cls._instance = super(JsonInspectorSingleton, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, filepath):
        if not self._initialized:
            self.filepath = filepath
            self.data = None
            self._initialized = True

    def load(self):
        if not os.path.exists(self.filepath):
            print(f"[ERROR] El archivo '{self.filepath}' no existe.")
            return False
        try:
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)
            return True
        except json.JSONDecodeError:
            print("[ERROR] El archivo no contiene un JSON válido.")
            return False
        except Exception as e:
            print(f"[ERROR] Ocurrió un problema al leer el archivo: {e}")
            return False

    def inspect_keys(self, keys):
        if self.data is None:
            print("[ERROR] Los datos no han sido cargados.")
            return
        for key in keys:
            value = self.data.get(key)
            if value is not None:
                print(f"{key}: {value}")
            else:
                print(f"{key} no encontrado en el archivo JSON")


def mostrar_ayuda():
    print("Uso:")
    print("  python getJson_ref_poo.py archivo.json [clave1 clave2 ...]")
    print("Ejemplo:")
    print("  python getJson_ref_poo.py datos.json token1 token2")


# Bloque principal de ejecución
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] Falta el nombre del archivo JSON.")
        mostrar_ayuda()
    else:
        archivo_json = sys.argv[1]
        claves = sys.argv[2:] if len(sys.argv) > 2 else ['token1', 'token2']

        inspector = JsonInspectorSingleton(archivo_json)
        if inspector.load():
            inspector.inspect_keys(claves)
        else:
            print("[INFO] Finalizando el programa por error en la carga del archivo.")
