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
    print("5. Ver listado de aparatos")
    print("0. Salir")

def leer_float(mensaje):
    """Valida que el usuario ingrese un número válido y positivo"""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")

while True:
    menu()
    opcion = input("Ingrese su opción: ")

    if opcion == "0":
        print("Saliendo del sistema... 👋")
        break

    elif opcion == "5":
        SistemaConsumo.mostrar_registros()
        SistemaConsumo.resumen_total()

    elif opcion in ["1", "2", "3", "4"]:
        potencia = leer_float("Ingrese potencia en watts: ")
        horas = leer_float("Ingrese horas de uso diario: ")
        tarifa = leer_float("Ingrese costo por kWh en $: ")

        if opcion == "1":
            aparato = Refrigerador(potencia, horas, tarifa)
        elif opcion == "2":
            aparato = Televisor(potencia, horas, tarifa)
        elif opcion == "3":
            aparato = AireAcondicionado(potencia, horas, tarifa)
        elif opcion == "4":
            aparato = Iluminacion(potencia, horas, tarifa)

        SistemaConsumo.agregar_aparato(aparato)
        print(f"{aparato.nombre} agregado con éxito")

    else:
        print("Opción inválida, intente de nuevo.")

# Al salir, mostrar reportes finales
SistemaConsumo.mostrar_registros()
SistemaConsumo.resumen_total()
