import socket
import json
import argparse
import sys
import uuid
import logging
import time

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 8080
RECONNECT_INTERVAL = 30 # segundos (parametrizable según consigna)

def configure_logging(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s - ObserverClient - %(levelname)s - %(message)s')

def get_cpu_uuid():
    return hex(uuid.getnode())

def run_observer_client(host, port, output_file=None, verbose=False):
    configure_logging(verbose)
    
    uuid_client = get_cpu_uuid()
    subscribe_request = {
        "UUID": uuid_client,
        "ACTION": "subscribe"
    }
    subscribe_message = json.dumps(subscribe_request).encode('utf-8')
    logging.info(f"Observer Client iniciado con UUID: {uuid_client}")

    while True:
        client_socket = None
        try:
            # 1. Conectar y Suscribir
            logging.info(f"Intentando conectar a {host}:{port} y suscribirse...")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            
            client_socket.sendall(subscribe_message)
            logging.debug("Mensaje de subscripción enviado.")
            
            # Recibir la respuesta de confirmación de subscripción (consume la primera respuesta)
            confirmation = client_socket.recv(4096)
            if confirmation:
                logging.info(f"Subscripción confirmada: {confirmation.decode('utf-8')}")

            # 2. Esperar Notificaciones
            logging.info("Subscrito con éxito. Esperando notificaciones (manteniendo socket abierto)...")
            
            while True:
                # El socket debe permanecer abierto. Esperamos activamente datos.
                data = client_socket.recv(4096)
                if not data:
                    # Conexión cerrada por el servidor
                    logging.warning("Conexión perdida (socket cerrado por el servidor o red).")
                    break # Sale del bucle interno para reintentar la conexión
                
                try:
                    notification_json = json.loads(data.decode('utf-8'))
                    
                    # Mostrar la notificación por salida estándar
                    output_text = json.dumps(notification_json, indent=4)
                    print("\n--- NOTIFICACIÓN RECIBIDA (CORPORATEDATA UPDATE) ---")
                    print(output_text)
                    print("---------------------------------------------------\n")
                    
                    # Guardar en archivo si se especificó
                    if output_file:
                        with open(output_file, 'a') as f: 
                            f.write(output_text + "\n")
                        logging.info(f"Notificación guardada en {output_file}")

                except json.JSONDecodeError:
                    logging.error(f"Error: Notificación recibida no es un JSON válido: {data.decode('utf-8')}")
                
        
        except ConnectionRefusedError:
            logging.error(f"Error de conexión: El servidor en {host}:{port} no está disponible.")
        except Exception as e:
            # Manejar cualquier otra excepción (ej. fallo de red, error de I/O)
            logging.error(f"Error inesperado en el cliente Observer: {e}")
            
        finally:
            if client_socket:
                client_socket.close()
            
        # 3. Reintento periódico
        logging.info(f"Esperando {RECONNECT_INTERVAL} segundos antes de reintentar la conexión...")
        time.sleep(RECONNECT_INTERVAL)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ObserverClient: Suscriptor a cambios de datos corporativos.")
    parser.add_argument("-s", "--hostname", default=DEFAULT_HOST, help=f"Host del servidor (default: {DEFAULT_HOST}).")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT, help=f"Puerto del servidor (default: {DEFAULT_PORT}).")
    parser.add_argument("-o", "--output", help="Ruta al archivo donde se registrarán las notificaciones (modo 'append').")
    parser.add_argument("-v", "--verbose", action="store_true", help="Activar mensajes de trace/debug.")
    
    args = parser.parse_args()
    
    run_observer_client(args.hostname, args.port, args.output, args.verbose)