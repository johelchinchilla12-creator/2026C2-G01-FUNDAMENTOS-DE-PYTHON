"""Programa principal del proyecto modular BCCR"""

from lectura_datos import URL_BCCR, cargar_tabla_bccr
from limpieza_datos import (
    filtrar_por_tipo_entidad,
    limpiar_datos,
    mostrar_diferencial_alto,
)


def mostrar_primeras_entidades(datos):
    """Muestra unba vista de las columnas principales"""
    columnas = ["ENTIDAD", "COMPRA", "VENTA", "DIFERENCIAL"]
    print(datos[columnas].head().to_string(index=False))


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
            filtrado = filtrar_por_tipo_entidad(datos)
            print(filtrado.to_string())
        elif opcion == "4":
            pass
        elif opcion == "5":
            filtrado = filtrar_por_tipo_entidad(datos)
            filtrado.plot.bar(
                y="DIFERENCIAL",
                title="Diferencial promedio por tipo de entidad",
                legend=False,
            )
            filtrado.plot.bar(
                y="COMPRA", title="Compra promedio por tipo de entidad", legend=False
            )
            filtrado.plot.bar(
                y="VENTA", title="Venta promedio por tipo de entidad", legend=False
            )

        elif opcion == "6":
            print("\nAnalisis finalizado ")
            input("Presione enter para salir.....")
            break
        else:
            print("\nOpcion no valida, escriba un numero del 1 al 6")
        input("Presione enter para continuar.....")


if __name__ == "__main__":
    ejecutar()
