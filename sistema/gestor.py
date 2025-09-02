# gestor.py
class SistemaConsumo:
    listado = []

    @classmethod
    def agregar_aparato(cls, aparato):
        cls.listado.append(aparato)

    @classmethod
    def mostrar_registros(cls):
        print("\n--- Aparatos registrados ---")
        for i, aparato in enumerate(cls.listado, 1):
            print(f"{i}. {aparato.nombre} - {aparato.potencia}W - {aparato.horas}h/día")
            print(f"   Consumo mensual: {aparato.consumo_mensual_kwh():.2f} kWh - "
                  f"Costo: ${aparato.costo_mensual():.2f}")
        print("---------------------------")

    @classmethod
    def resumen_total(cls):
        total_consumo = sum(a.consumo_mensual_kwh() for a in cls.listado)
        total_costo = sum(a.costo_mensual() for a in cls.listado)
        print("\n=== Resumen total ===")
        print(f"Consumo total: {total_consumo:.2f} kWh")
        print(f"Costo total: ${total_costo:.2f}")
        print("=====================")