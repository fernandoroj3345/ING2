"""Módulo para acceso y manipulación de datos en DynamoDB usando patrón Singleton."""

import threading
import logging
import boto3
#from boto3.dynamodb.conditions import Key

class DynamoDBConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance.dynamodb = boto3.resource('dynamodb')
        return cls._instance

    def get_table(self, table_name):
        return self.dynamodb.Table(table_name)


# Funciones para manejo básico de CorporateData
def get_corporate_data(id):
    db = DynamoDBConnection()
    table = db.get_table('CorporateData')
    try:
        response = table.get_item(Key={'id': id})
        return response.get('Item', None)
    except Exception as e:
        logging.error(f"Error al obtener CorporateData para {id}: {e}")
        return None

def set_corporate_data(data_dict):  # <-- renombrado si cambiaste en todo el proyecto
    db = DynamoDBConnection()
    table = db.get_table('CorporateData')
    try:
        table.put_item(Item=data_dict)
        return True
    except Exception as e:
        logging.error(f"Error al guardar CorporateData: {e}")
        return False

def list_corporate_data():
    db = DynamoDBConnection()
    table = db.get_table('CorporateData')
    try:
        response = table.scan()
        return response.get('Items', [])
    except Exception as e:
           logging.error(f"Error al buscar log por session_id {session_id}: {e}")
           return []

def save_log(uuid, session_id, action, details=None):
    import time
    db = DynamoDBConnection()
    table = db.get_table('CorporateLog')
    item = {
        # 1. GENERAR UN ID ÚNICO PARA LA CLAVE PRIMARIA REQUERIDA
        'id': str(uuid) + "-" + str(time.time()), 
        'uuid': str(uuid),
        'session_id': session_id,
        'action': action,
        'timestamp': int(time.time()),
        'details': details or {}
    }
    try:
        table.put_item(Item=item)
        return True
    except Exception as e:
        logging.error(f"Error al guardar log: {e}")
        return False



def get_log_by_session(session_id):
    """Recupera logs usando el session_id como clave, lo cual requiere un Scan filtrado."""
    db = DynamoDBConnection()
    table = db.get_table('CorporateLog')
    
    try:
        from boto3.dynamodb.conditions import Key
        response = table.scan(
            FilterExpression=Key('session_id').eq(session_id)
        )
        return response.get('Items', [])
    except Exception as e:
        import logging
        logging.error(f"Error al buscar log por session_id {session_id}: {e}")
        return []

