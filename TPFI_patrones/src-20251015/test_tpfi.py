import unittest
from unittest import mock
import json
import uuid
import time

# Importo las funciones que quiero probar/simular
from db_access import DynamoDBConnection, save_log 
from tcp import SingletonServer 

# --- Test de Patrones de Conexión (El que ya tengo) ---
class TestPatrones(unittest.TestCase):
    def test_dynamodb_connection_singleton(self):# instancia de la clase
        # Verifica el patrón Singleton de la conexión
        conn1 = DynamoDBConnection()
        conn2 = DynamoDBConnection()
        self.assertIs(conn1, conn2, "DynamoDBConnection NO es un Singleton")
        self.assertIsNotNone(conn1.dynamodb)

# --- Test de Auditoría y Proxy (Verificación de CorporateLog) ---
class TestAuditoria(unittest.TestCase):
    
    # Preparo un objeto de solicitud de prueba
    TEST_UUID = "TEST-CLIENT-UUID"
    TEST_ID = "TEST-ID-999"

    def setUp(self):
        # Inicializo una instancia del servidor para simular el manejo de clientes
        # Uso un puerto no estándar (8081) para evitar conflicto si tcp.py está corriendo
        self.server = SingletonServer(port=8081) 
        
    @mock.patch('db_access.save_log') 
    @mock.patch('db_access.get_corporate_data')
    def test_logueo_en_accion_get(self, mock_get_data, mock_save_log):
        """Verifica que la acción 'get' llame a save_log con los parámetros correctos."""
        
        # 1. Configurar la simulación (Mock): 
        #    Hago que get_corporate_data retorne un valor para simular éxito
        mock_get_data.return_value = {"id": self.TEST_ID, "address": "Test Address"}
        
        # 2. Preparar la solicitud JSON simulada
        request_data = {
            "UUID": self.TEST_UUID,
            "ID": self.TEST_ID,
            "ACTION": "get"
        }
        
               
        session_id = str(uuid.uuid4())
        save_log_success = save_log(self.TEST_UUID, session_id, "get", {"ID": self.TEST_ID})
        
        # Verificación: Esto solo asegura que la función se ejecutó sin errores
        self.assertTrue(save_log_success, "La función save_log no pudo guardar el registro.")
             
        
        request_json = json.dumps(request_data)
        
        
from db_access import DynamoDBConnection, save_log, get_log_by_session 

# ... (Clase TestPatrones) ...

# --- Test de Auditoría (Verificación REAL en CorporateLog) ---
class TestAuditoria(unittest.TestCase):
    
    TEST_UUID = "TEST-LOG-AUDIT"

    def test_integracion_auditoria_save_log(self):
        """Test de integración: Ejecuta save_log y consulta CorporateLog para verificar la entrada."""
        
        # 1. Generar datos únicos para la prueba
        test_session_id = "SESSION-" + str(uuid.uuid4())
        test_action = "SET_AUDITORIA_TEST"
        
        # 2. Ejecutar la acción de logueo (¡Llama a la función REAL!)
        log_details = {"ID": "AUDIT-001", "Data": "Test"}
        log_success = save_log(self.TEST_UUID, test_session_id, test_action, log_details)
        
        # 3. Primer Aserción: Verificar que la llamada a DB NO falló
        self.assertTrue(log_success, "ERROR: save_log devolvió False. Problema de AWS (credenciales/tabla) o código interno.")
        
        # 4. Esperar un momento (Consistencia eventual de DynamoDB)
        time.sleep(1) 
        
        # 5. Consultar CorporateLog usando la función importada
        logs = get_log_by_session(test_session_id) 
        
        # 6. Aserciones (Verificación de la entrada)
        self.assertTrue(len(logs) > 0, f"No se encontró el registro de auditoría con session_id: {test_session_id}")
        
        # Verificar los campos guardados
        registro = logs[0]
        self.assertEqual(registro.get('uuid'), self.TEST_UUID)
        self.assertEqual(registro.get('action'), test_action)
        self.assertEqual(registro.get('session_id'), test_session_id)
        
        pass # Reemplaza esto con la lógica real de consulta a CorporateLog

if __name__ == '__main__':
    unittest.main()
