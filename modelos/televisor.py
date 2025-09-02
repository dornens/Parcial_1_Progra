# televisor.py
from modelos.aparato import AparatoElectrico

class Televisor(AparatoElectrico):
    def __init__(self, potencia_watts, horas_uso_diario, tarifa_kwh):
        super().__init__("Televisor", potencia_watts, horas_uso_diario, tarifa_kwh)
