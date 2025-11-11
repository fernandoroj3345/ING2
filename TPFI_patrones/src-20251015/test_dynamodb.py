"""
Este test asegura que mi módulo y credenciales funcionan y
que puedo operar sobre la tabla esperada desde mi código Python.
"""

from db_access import get_corporate_data, set_corporate_data, list_corporate_data

# Prueba: insertar un registro básico
test_item = {
    'id': 'TEST-CONN',
    'address': 'Prueba 123',
    'cuit': '00-00000000-0',
    'phone': '123456789',
    'sequence_id': '9999'
}
print("Insertando registro de prueba...")
insert_ok = set_corporate_data(test_item)
print("Resultado de inserción:", insert_ok)

# Prueba: obtener el registro recién insertado
print("Recuperando registro de prueba...")
retrieved = get_corporate_data('TEST-CONN')
print("Registro recuperado:", retrieved)

# Prueba: listar todos los registros existentes en la tabla
print("Listando registros en tabla CorporateData...")
all_items = list_corporate_data()
print("Total registros recuperados:", len(all_items))
print("Ejemplo primer registro:", all_items[0] if all_items else "Sin registros")
