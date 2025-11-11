#!/usr/bin/env python3
import json
import sys
import os
from abc import ABC, abstractmethod

# 1 Interfaz común
class JsonInspectorBase(ABC):
    @abstractmethod
    def load(self):
        """Carga el JSON desde self.filepath; retorna True/False según éxito."""
        pass

    @abstractmethod
    def inspect_keys(self, keys):
        """Inspecciona las claves dadas y las imprime."""
        pass


# 2a) Implementación funcional (script “plano”)
class FunctionalInspector(JsonInspectorBase):
    def __init__(self, filepath):
        self.filepath = filepath
        self.obj = None

    def load(self):
        if not os.path.exists(self.filepath):
            print(f"[ERROR] El archivo '{self.filepath}' no existe.")
            return False
        try:
            with open(self.filepath, 'r') as f:
                data = f.read()
            self.obj = json.loads(data)
            return True
        except json.JSONDecodeError:
            print("[ERROR] JSON inválido en el archivo.")
            return False
        except Exception as e:
            print(f"[ERROR] Falló al leer el archivo: {e}")
            return False

    def inspect_keys(self, keys):
