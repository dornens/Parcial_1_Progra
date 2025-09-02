# aire_acondicionado.py
from modelos.aparato import AparatoElectrico

class AireAcondicionado(AparatoElectrico):
    def __init__(self, potencia_watts, horas_uso_diario, tarifa_kwh):
        super().__init__("Aire Acondicionado", potencia_watts, horas_uso_diario, tarifa_kwh)
