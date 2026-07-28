"""Programa principal del proyecto modular BCCR"""

from lectura_datos import URL_BCCR, cargar_tabla_bccr
from limpieza_datos import limpiar_datos


def mostrar_primeras_entidades():
    """Muestra una vista de las columnas principales"""
    columnas = ["Entidadd, Compra, Venta, Diferencial"]
    print(datos[columnas].head(10).to_string(index=False))


def ejecutar():
    datos_crudos = cargar_tabla_bccr(URL_BCCR)
    datos = limpiar_datos(datos_crudos)
    print("Datos cargados exitosamente de https//gee.bccr.fi.cr/")
    while True:
        print("nPROYECTO DE ANALISIS DE DATOS DEL BCCR")
        print("1.Mostrar primeras entidades limpias")
        print("2.Mostrar entidades con diferencial superior al promedio")
        print("3.Promedio por entidad  ")
        print("4.Mostrar lista entidades")
        print("5.Graficar")
        print("6.Salir")

        opcion = input("Ingrese la opcion del menu ").lower().strip()
        if opcion == "1":
            mostrar_primeras_entidades(datos)
        elif opcion == "2":
            resultado = mostrar_diferencial_alto(datos)
            resultado = resultado.sort_values(by="Diferencial", ascending=False)
            mostrar_primeras_entidades(resultado)
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            print("\nAnalisis finalizado ")
            input("Presione enter para salir.....")
            break
        else:
            print("\nOpcion no valida, escriba un numero del 1 al 6")
        input("Presione enter para continuar.....")


if __name__ == "__main__":
    ejecutar()
