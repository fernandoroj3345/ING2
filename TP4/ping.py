import subprocess

class Ping:
    def __init__(self):
        pass

    def _ejecutar_ping(self, ip_address):
        for i in range(10):
            try:
                resultado = subprocess.run(['ping', '-c', '1', ip_address], capture_output=True, text=True, timeout=1)
                if resultado.returncode == 0:
                    print(f"Ping exitoso a {ip_address} (Intento {i+1})")
                else:
                    print(f"Fallo el ping a {ip_address} (Intento {i+1}): {resultado.stderr.strip()}")
            except subprocess.TimeoutExpired:
                print(f"Tiempo de espera agotado al hacer ping a {ip_address} (Intento {i+1})")
            except FileNotFoundError:
                print("Error: El comando 'ping' no se encontró. Asegúrate de que esté en tu PATH.")
                return

    def execute(self, ip_address):
        if ip_address.startswith("192."):
            print(f"Realizando 10 pings a {ip_address} (con validación)...")
            self._ejecutar_ping(ip_address)
        else:
            print("Error: La dirección IP debe comenzar con '192.'.")

    def executefree(self, ip_address):
        print(f"Realizando 10 pings a {ip_address} (sin validación)...")
        self._ejecutar_ping(ip_address)

class PingProxy:
    def __init__(self):
        self._real_ping = Ping()

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            print(f"Detectada dirección especial '{ip_address}'. Redirigiendo ping a www.google.com...")
            self._real_ping.executefree("www.google.com")
        else:
            print(f"Redirigiendo ping a través de la clase Ping para la dirección: {ip_address}")
            self._real_ping.execute(ip_address)

# Ejemplo de uso
if __name__ == "__main__":
    ping_directo = Ping()
    ping_proxy = PingProxy()

    print("\nProbando la clase Ping directamente:")
    ping_directo.execute("192.168.1.1")
    ping_directo.execute("10.0.0.1")
    ping_directo.executefree("www.example.com")

    print("\nProbando la clase PingProxy:")
    ping_proxy.execute("192.168.0.254")
    ping_proxy.execute("192.168.1.5")
    ping_proxy.execute("10.0.0.10")