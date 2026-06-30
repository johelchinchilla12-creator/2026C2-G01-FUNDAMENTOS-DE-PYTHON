"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes


def calcular_total(ventas):
    """Recibo una lista, la sumo y retorno el total"""
    return sum(ventas)


def calcular_promedio(lista):
    """Retorna el promedio de ventas de una lista"""
    return sum(lista) / len(lista)


def calcular_porcentaje(total, meta, formato=False):
    porcentaje = total / meta * 100
    if formato:
        return f"{porcentaje:.2f}%"
    return porcentaje


def calcular_clasificacion(total, meta):
    porcentaje_sede = calcular_porcentaje(total, meta)
    if porcentaje_sede >= 100:
        mensaje_sede = "Meta alcanzada."
    elif porcentaje_sede >= 80:
        mensaje_sede = "Meta casi alcanzada, prestar atención."
    else:
        mensaje_sede = "Meta no alcanzada URGE ATENCION."
    return mensaje_sede


def formato_colones(monto):
    """Formatea un número como colones con separador de miles"""
    return f"₡{monto:,.0f}"


for sede in sedes:
    nombre = sede["nombre"]
    ventas = sede["ventas"]
    meta = sede["meta"]

    total = calcular_total(ventas)
    promedio = calcular_promedio(ventas)
    porcentaje = calcular_porcentaje(total, meta, formato=True)
    estado = calcular_clasificacion(total, meta)

    print(f"--- {nombre} ---")
    print(f"  Total:      {formato_colones(total)}")
    print(f"  Promedio:   {formato_colones(promedio)}")
    print(f"  Porcentaje: {porcentaje}")
    print(f"  Estado:     {estado}")


provincias = []
for sede in sedes:
    if sede["provincia"] not in provincias:
        provincias.append(sede["provincia"])

print("\nProvincias:", provincias)


print("\nReporte por emprendimiento:")
for sede in sedes:
    total = calcular_total(sede["ventas"])
    promedio = calcular_promedio(sede["ventas"])
    estado = calcular_clasificacion(total, sede["meta"])
    print(
        f"  {sede['nombre']} ({sede['tipo']}, {sede['provincia']}): total={formato_colones(total)}, promedio={formato_colones(promedio)}, estado={estado}"
    )


sede_top = None
total_top_sede = 0

for sede in sedes:
    total_sede = calcular_total(sede["ventas"])
    if total_sede > total_top_sede:
        sede_top = sede["nombre"]
        total_top_sede = total_sede

print(
    f"\nEl emprendimiento que más vendió es {sede_top} con un total de {formato_colones(total_top_sede)}."
)

ingresos_por_provincia = {}

for sede in sedes:
    provincia = sede["provincia"]
    total_sede = calcular_total(sede["ventas"])

    if provincia in ingresos_por_provincia:
        ingresos_por_provincia[provincia] += total_sede
    else:
        ingresos_por_provincia[provincia] = total_sede

print("\nIngresos por provincia:")
for provincia, total in ingresos_por_provincia.items():
    print(f"  {provincia}: {formato_colones(total)}")


provincia_top = None
total_top = 0

for provincia, total in ingresos_por_provincia.items():
    if total > total_top:
        provincia_top = provincia
        total_top = total

print(
    f"\nLa provincia con más ingresos es {provincia_top} con un total de {formato_colones(total_top)}."
)
# audita el coidgo, dime mejoras y que se puede optimizar, varias versiones
