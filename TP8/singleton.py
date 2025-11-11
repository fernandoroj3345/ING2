
import json
import threading
import sys

class BancoManager: # SINGLETON
    _instance = None  # ← Almacena la única instancia de la clase
    _lock = threading.Lock() # ← Aseguro acceso seguro en entornos multihilo

    def __new__(cls, jsonfile):  # ← Sobrescribe el método para controlar la creación
        with cls._lock:
            if cls._instance is None: # ← Si no hay instancia todavía..
                cls._instance = super().__new__(cls) # ← ... la créo
                cls._instance._load_data(jsonfile) # ← ...y cargo los datos
            return cls._instance # ← Devuelve la instancia única existente

    def _load_data(self, jsonfile):
        with open(jsonfile, 'r') as file:
            self.data = json.load(file)

    def seleccionar_token(self, monto):
        # Filtrar los tokens con saldo suficiente
        disponibles = {
            token: info for token, info in self.data.items()
            if info["saldo"] >= monto
        }

        if not disponibles:
            raise Exception("No hay bancos con saldo suficiente.")

        # Elegir el token con menos pagos realizados
        seleccionado = min(disponibles.items(), key=lambda x: x[1]["pagos_realizados"])
        token = seleccionado[0]
        clave = seleccionado[1]["clave"]
        return token, clave

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python getJson.py sitedata.json monto")
        sys.exit(1)

    jsonfile = sys.argv[1]
    monto = float(sys.argv[2])

    gestor = BancoManager(jsonfile)
    token, clave = gestor.seleccionar_token(monto)

    print(f"Token seleccionado automáticamente: {token}")
    print(f"Clave del banco: {clave}")
