import uuid
import platform

class CorporateDataEntry:
    def __init__(self, id, address, cuit, phone, sequence_id):
        self.id = id
        self.address = address
        self.cuit = cuit
        self.phone = phone
        self.sequence_id = sequence_id

class CorporateLogEntry:
    def __init__(self, uuid, session_id, action, timestamp, details=None):
        self.uuid = uuid
        self.session_id = session_id
        self.action = action
        self.timestamp = timestamp
        self.details = details or {}

def get_cpu_identifier():
    # Devuelve el número único de la "CPU"
    return uuid.getnode()

def get_system_info():
    # Devuelve información relevante del sistema (para auditoría)
    return {
        'platform': platform.system(),
        'platform-release': platform.release(),
        'platform-version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor()
    }
