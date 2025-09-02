# aparato.py
class AparatoElectrico:
    def __init__(self, nombre, potencia_watts, horas_uso_diario, tarifa_kwh):
        self.nombre = nombre
        self.potencia = potencia_watts
        self.horas = horas_uso_diario
        self.tarifa = tarifa_kwh

    def consumo_diario_kwh(self):
        return (self.potencia * self.horas) / 1000

    def consumo_mensual_kwh(self, dias=30):
        return self.consumo_diario_kwh() * dias

    def costo_mensual(self, dias=30):
        return self.consumo_mensual_kwh(dias) * self.tarifa
