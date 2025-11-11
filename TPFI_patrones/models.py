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
    # Devuelve el número único de mi "CPU"
    return uuid.getnode()

def get_system_info():
    # Me Devuelve información relevante del sistema (para auditoría)
    return {
        'platform': platform.system(),
        'platform-release': platform.release(),
        'platform-version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor()
    }

if __name__ == "__main__":
    print("Identificador único CPU (MAC, UUID):", get_cpu_identifier())
    print("Información del sistema:", get_system_info())

    # Ejemplo de instanciación de CorporateDataEntry
    ejemplo = CorporateDataEntry(
        id="UADER-FCyT-IS2",
        address="25 de Mayo 385-1P",
        cuit="30-70925411-8",
        phone="03442 43-1442",
        sequence_id="1146"
    )
    print("Ejemplo CorporateDataEntry:", ejemplo.__dict__)



