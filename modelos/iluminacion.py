# iluminacion.py
from modelos.aparato import AparatoElectrico

class Iluminacion(AparatoElectrico):
    def __init__(self, potencia_watts, horas_uso_diario, tarifa_kwh):
        super().__init__("Iluminación", potencia_watts, horas_uso_diario, tarifa_kwh)
