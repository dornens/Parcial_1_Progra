# main.py
from modelos.refrigerador import Refrigerador
from modelos.televisor import Televisor
from modelos.aire_acondicionado import AireAcondicionado
from modelos.iluminacion import Iluminacion
from sistema.gestor import SistemaConsumo

def menu():
    print("\nSeleccione un aparato eléctrico:")
    print("1. Refrigerador")
    print("2. Televisor")
    print("3. Aire Acondicionado")
    print("4. Iluminación")
    print("0. Salir")

while True:
    menu()
    opcion = input("Ingrese su opción: ")

    if opcion == "0":
        break

    if opcion in ["1", "2", "3", "4"]:
        potencia = float(input("Ingrese potencia en watts: "))
        horas = float(input("Ingrese horas de uso diario: "))
        tarifa = float(input("Ingrese costo por kWh en $: "))

        if opcion == "1":
            aparato = Refrigerador(potencia, horas, tarifa)
        elif opcion == "2":
            aparato = Televisor(potencia, horas, tarifa)
        elif opcion == "3":
            aparato = AireAcondicionado(potencia, horas, tarifa)
        elif opcion == "4":
            aparato = Iluminacion(potencia, horas, tarifa)

        SistemaConsumo.agregar_aparato(aparato)
        print(f"{aparato.nombre} agregado con éxito ✅")

    else:
        print("Opción inválida, intente de nuevo.")

# Al finalizar, mostrar reportes
SistemaConsumo.mostrar_registros()
SistemaConsumo.resumen_total()
