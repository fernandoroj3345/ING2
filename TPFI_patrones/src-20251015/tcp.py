"""Servidor TCP Singleton/Proxy/Observer para acceso a servicios AWS DynamoDB."""
"""El patrón Singleton en un servidor cumple la función de asegurar que solo exista una única 
instancia de una clase y proporciona un punto de acceso global a esa instancia"""

import socket
import threading
import json
import logging
from db_access import *
import uuid
from decimal import Decimal

def decimal_default_converter(obj):
    """Convierte objetos Decimal a float para serialización JSON."""
    if isinstance(obj, Decimal):
        # Conversión a float. Si se necesita precisión, se puede convertir a str(obj).
        return float(obj)
    raise TypeError


class SingletonServer:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, host='localhost', port=8080):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance.host = host
                    cls._instance.port = port
                    cls._instance.clients = []
                    cls._instance.observers = []   # para observer
                    cls._instance.running = False
                    cls._instance.server_socket = None
        return cls._instance

    def start_server(self):
        if self.running:
            logging.warning("Servidor ya está corriendo")
            return
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = True
        logging.info(f"Servidor iniciado en {self.host}:{self.port}")
        thread = threading.Thread(target=self.accept_clients)
        thread.start()

    def accept_clients(self):
        while self.running:
            client_socket, addr = self.server_socket.accept()
            logging.info(f"Conexión aceptada de {addr}")
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket, addr)).start()

    def handle_client(self, client_socket, addr):
        try:
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                try:
                    request = json.loads(data.decode())
                    logging.info(f"Recibido de {addr}: {request}")

                    uuid_client = request.get("UUID", "unknown")
                    action = request.get("ACTION", "").lower()
                    session_id = str(uuid.uuid4())

                    response = {}
                    if action == "get":
                        id_req = request.get("ID")
                        if not id_req:
                            response = {"Error": "Falta campo ID"}
                        else:
                            data = get_corporate_data(id_req)
                            response = data if data else {"Error": "No encontrado"}
                        save_log(uuid_client, session_id, "get", {"ID": id_req})

                    elif action == "set":
                        # Utilizo el ID del request para la clave
                        id_req = request.get("ID")
                        # Creo una copia de los datos para el log/notificación sin las claves de control (UUID, ACTION)
                        data_to_set = {k: v for k, v in request.items() if k.lower() not in ["uuid", "action"]}
                        if not id_req:
                            response = {"Error": "Falta campo ID"}
                        else:
                            # Aseguramos que 'id' esté en los datos si es la clave de DynamoDB
                            data_to_set['id'] = id_req 
                            put_success = set_corporate_data(data_to_set)
                            if put_success:
                                response = data_to_set 
                                
                                # Implementación clave del Observer: Notifico a los clientes
                                self.notify_observers(response) 
                            else:
                                response = {"Error": "Falla al almacenar"}
                        
                        # Generar el log después de la acción
                        save_log(uuid_client, session_id, "set", {"ID": id_req})

                    elif action == "list":
                        data_list = list_corporate_data()
                        response = data_list if data_list else {"Error": "Tabla vacía o falla"}
                        save_log(uuid_client, session_id, "list", {})

                    elif action == "subscribe":
                        if client_socket not in self.observers:
                            self.observers.append(client_socket)
                            logging.info(f"Cliente {addr} suscripto a notificaciones")
                        response = {"Info": "Subscripción aceptada"}
                        save_log(uuid_client, session_id, "subscribe", {})

                    else:
                        response = {"Error": "Acción no soportada"}

                    response_json = json.dumps(response, default=decimal_default_converter).encode()
                    client_socket.sendall(response_json)

                    if action != "subscribe":
                        break

                except json.JSONDecodeError:
                    error_msg = json.dumps({"Error": "JSON inválido recibido"}).encode()
                    client_socket.sendall(error_msg)
        finally:
            client_socket.close()
            if client_socket in self.clients:
                self.clients.remove(client_socket)
            if client_socket in self.observers:
                self.observers.remove(client_socket)
            logging.info(f"Conexión cerrada de {addr}")

    def notify_observers(self, data):
        notification = json.dumps(data).encode()
        for observer in list(self.observers):
            try:
                observer.sendall(notification)
            except Exception as e:
                logging.error(f"Fallo notificación a observer: {e}")
                self.observers.remove(observer)

    def stop_server(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        for client in self.clients:
            client.close()
        self.clients = []
        logging.info("Servidor detenido")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    server = SingletonServer(port=8080)
    server.start_server()
