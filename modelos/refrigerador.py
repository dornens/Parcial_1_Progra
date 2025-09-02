# refrigerador.py
from modelos.aparato import AparatoElectrico

class Refrigerador(AparatoElectrico):
    def __init__(self, potencia_watts, horas_uso_diario, tarifa_kwh):
        super().__init__("Refrigerador", potencia_watts, horas_uso_diario, tarifa_kwh)
