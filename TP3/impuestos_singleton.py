# impuestos_singleton.py

class CalculadoraImpuestos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instancia

    def calcular_total_impuestos(self, base_imponible):
        if not isinstance(base_imponible, (int, float)) or base_imponible < 0:
            raise ValueError("La base imponible debe ser un número positivo")

        iva = base_imponible * 0.21       # 21%
        iibb = base_imponible * 0.05      # 5%
        contribuciones = base_imponible * 0.012  # 1.2%

        total_impuestos = iva + iibb + contribuciones
        return total_impuestos


# Ejemplo de uso
if __name__ == "__main__":
    calculadora1 = CalculadoraImpuestos()
    calculadora2 = CalculadoraImpuestos()

    base = 1000
    total = calculadora1.calcular_total_impuestos(base)
    print(f"Base imponible: ${base}")
    print(f"Total impuestos: ${total:.2f}")
    print(f"Misma instancia: {'Sí' if calculadora1 is calculadora2 else 'No'}")

#incluyo en la clase
#IVA (21%)

#IIBB (5%)

#Contribuciones municipales (1.2%)

#Protección contra valores negativos o tipos no numéricos.

#Aplicación del patrón Singleton para compartir la misma instancia en todo el sistema.