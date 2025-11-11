import socket
import json
import argparse
import sys
import uuid
import logging
import platform

HOST = 'localhost' # Valor por defecto
PORT = 8080        # Valor por defecto

def configure_logging(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s - SingletonClient - %(levelname)s - %(message)s')

def get_cpu_uuid():
    # Obtener un UUID único para la CPU (getnode() retorna la MAC address en un int)
    return hex(uuid.getnode())

def run_client(input_file, output_file=None, verbose=False, host=HOST, port=PORT):
    configure_logging(verbose)
    
    try:
        with open(input_file, 'r') as f:
            request_data = json.load(f)
    except FileNotFoundError:
        logging.error(f"Error: Archivo de entrada {input_file} no encontrado.")
        return
    except json.JSONDecodeError:
        logging.error(f"Error: Archivo de entrada {input_file} no es un JSON válido.")
        return
    
    # 1. Preparar la petición
    if "UUID" not in request_data:
        request_data["UUID"] = get_cpu_uuid()
    
    action = request_data.get("ACTION", "").lower()
    if action not in ["get", "set", "list"]:
        logging.error(f"Error: Acción '{action}' no válida en el JSON de entrada.")
        return

    if action in ["get", "set"] and "ID" not in request_data:
        logging.error("Error: Las acciones 'get'/'set' requieren el campo 'ID'.")
        return
    
    # Conexión y envío
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        
        message = json.dumps(request_data).encode('utf-8')
        client_socket.sendall(message)
        logging.debug(f"Petición enviada: {message.decode()}")

        # Recibir respuesta
        response_data = b""
        while True:
            chunk = client_socket.recv(4096)
            if not chunk:
                break
            response_data += chunk
            # Asumimos que la respuesta se recibe en un solo envío antes de que el servidor cierre
            # Mejorar manejo para respuestas grandes si fuera necesario, pero 4096 suele ser suficiente.

        response_json = json.loads(response_data.decode('utf-8'))
        logging.debug(f"Respuesta recibida: {response_data.decode()}")

        # 3. Salida
        output_str = json.dumps(response_json, indent=4)
        if output_file:
            with open(output_file, 'w') as f:
                f.write(output_str)
            logging.info(f"Respuesta guardada en {output_file}")
        else:
            print("\n--- Respuesta del Servidor ---")
            print(output_str)
            print("------------------------------\n")

    except ConnectionRefusedError:
        logging.error(f"Error de conexión: El servidor en {host}:{port} no está corriendo o rechaza la conexión.")
    except Exception as e:
        logging.error(f"Ocurrió un error inesperado durante la comunicación: {e}")
    finally:
        if 'client_socket' in locals():
            client_socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SingletonClient: Cliente para GET/SET/LIST de datos corporativos.")
    parser.add_argument("-i", "--input", required=True, help="Ruta al archivo JSON de entrada (input.json).")
    parser.add_argument("-o", "--output", help="Ruta al archivo JSON de salida (opcional).")
    parser.add_argument("-v", "--verbose", action="store_true", help="Activar mensajes de trace/debug.")
    
    # Opcionales para host/port, aunque la consigna no los pide, son útiles para la práctica
    parser.add_argument("--host", default=HOST, help=f"Host del servidor (default: {HOST}).")
    parser.add_argument("--port", type=int, default=PORT, help=f"Puerto del servidor (default: {PORT}).")
    
    args = parser.parse_args()
    
    run_client(args.input, args.output, args.verbose, args.host, args.port)