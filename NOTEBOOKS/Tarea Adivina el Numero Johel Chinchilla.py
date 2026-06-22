# %% [markdown]
# # TAREA - Adivina el número
# ## Semana 05 | Fundamentos de Python
# ### Profesor: Ing. Andrés Mena Abarca
# 
# **Nombre del estudiante:** Johel Chinchilla Oviedo
# 
# 
# ---
# 
# ## Propósito
# 
# Crear un juego corto que use variables, entrada de datos, conversión con
# `int()`, comparaciones, decisiones, la librería `random` y una primera
# introducción a `while True` y `break`.
# 
# Esta tarea es un adelanto controlado hacia Semana 06. Los ciclos se estudiarán
# con más detalle después; aquí interesa entender por qué un programa puede
# necesitar repetir instrucciones hasta que ocurra una condición de salida.
# 

# %% [markdown]
# ## 1. ¿Qué hacen `while True` y `break`?
# 
# Un ciclo `while` repite instrucciones mientras una condición sea verdadera.
# Cuando escribimos `while True`, la condición siempre es verdadera, así que el
# ciclo necesita una salida explícita. Esa salida se logra con `break`.
# 
# Use este patrón cuando no sabe de antemano cuántas veces se repetirá una
# acción. Por ejemplo: pedir una opción válida, esperar una palabra correcta o
# continuar un juego hasta que el usuario acierte.
# 

# %% [markdown]
# ## 2. Ejemplo corto: repetir hasta escribir una palabra
# 
# Ejecute el ejemplo y observe dónde aparece la salida del ciclo.
# 

# %%
while True:
    palabra = input("Escriba salir para terminar: ").strip().lower()

    if palabra == "salir":
        print("Programa finalizado.")
        break

    print("Todavía no termina.")


# %% [markdown]
# ## 3. Ejemplo corto: repetir hasta cumplir una condición numérica
# 
# Este ejemplo usa `int()` porque `input()` siempre recibe texto.
# 

# %%
while True:
    numero = int(input("Escriba un número mayor que 10: "))

    if numero > 10:
        print("Número aceptado.")
        break

    print("Debe intentar otra vez.")


# %% [markdown]
# ## 4. Mini introducción a la librería `random`
# 
# Python trae librerías listas para resolver tareas comunes. La librería
# `random` permite generar valores al azar. Para usarla, primero se importa y
# luego se llama una de sus funciones.
# 
# En este juego puede usar `random.randint(inicio, fin)` para crear un número
# secreto entero dentro de un rango.
# 

# %%
import random

numero_ejemplo = random.randint(1, 10)
print(f"Número generado: {numero_ejemplo}")


# %% [markdown]
# ## 5. Análisis antes de crear el juego
# 
# Responda antes de programar:
# 
# 1. ¿Qué dato se genera una sola vez al inicio del juego?
# El número secreto, generado con random.randint(1, 20) antes de que empiece el ciclo.
# 2. ¿Qué dato cambia en cada intento?
# El número que ingresa el usuario y el contador de intentos.
# 3. ¿Qué condición permite terminar el ciclo?
# Break
# 4. ¿Cómo calculará qué tan cerca está el intento del número secreto?
# Con abs(numero_secreto - numero), que siempre devuelve una distancia positiva sin importar si el intento es mayor o menor.
# 5. ¿Qué mensajes de temperatura recibirá el usuario para acercarse a la respuesta?
# Frío (distancia > 10), tibio (6–10), caliente (3–5) e hirviendo (1–2).
# 6. ¿Qué variable podría contar cuántos intentos realizó el usuario?
# La variable intentos, que empieza en 0 y suma 1 cada vez que el usuario ingresa un número válido dentro del rango.
# 

# %% [markdown]
# ## 6. Consigna: Adivina el número
# 
# Cree un juego llamado **Adivina el número: frío o caliente**.
# 
# El programa debe:
# 
# 1. Generar un número secreto al azar entre 1 y 20 usando `random.randint()`.
# 2. Pedir intentos al usuario hasta que acierte.
# 3. Convertir cada intento a número entero.
# 4. Comparar el intento con el número secreto.
# 5. Dar pistas de dirección: si el número secreto es mayor o menor que el intento.
# 6. Dar pistas de temperatura según la distancia al número secreto.
# 7. Felicitar al usuario cuando acierte.
# 8. Mostrar cuántos intentos realizó el usuario.
# 9. Terminar el ciclo con `break` cuando el usuario acierte.
# 
# ### Reglas de temperatura
# 
# Use la distancia entre el intento y el número secreto para crear pistas más
# creativas. La distancia debe ser siempre positiva.
# 
# Para calcular una distancia positiva puede usar `abs()`. Por ejemplo,
# `abs(3 - 8)` produce `5`, no `-5`.
# 
# Puede usar esta escala o proponer una equivalente:
# 
# | Distancia al número secreto | Pista sugerida |
# |---:|---|
# | `0` | Acertó. Termina el juego. |
# | `1` o `2` | Hirviendo: está casi encima del número. |
# | `3` a `5` | Caliente: está cerca. |
# | `6` a `10` | Tibio: va por buen camino, pero falta. |
# | Más de `10` | Frío: está lejos. |
# 
# Ejemplo de experiencia esperada:
# 
# ```text
# Intento: 4
# El número secreto es mayor. Pista: frío.
# 
# Intento: 13
# El número secreto es menor. Pista: caliente.
# 
# Intento: 11
# Correcto. Adivinó en 3 intentos.
# ```
# 
# ### Restricciones
# 
# - No utilice listas.
# - No utilice funciones propias.
# - No agregue validación de errores todavía.
# - No copie una plantilla: use los ejemplos como referencia, pero diseñe su
#   propia solución.
# 

# %% [markdown]
# ## 7. Plan de variables
# 
# Complete esta tabla antes de escribir el código.
# 
# | Variable que usará | Tipo esperado | ¿Qué representa? | ¿Cuándo cambia? |
# |---|---|---|---|
# | numero_secreto | int | El número al azar que el usuario debe adivinar | Solo al inicio, una única vez |
# | intentos | int | Contador de intentos válidos realizados | Suma 1 en cada intento válido dentro del rango |
# | entrada | str | Texto crudo ingresado por el usuario | En cada vuelta del ciclo |
# | numero | int | El intento convertido a entero para comparar | n cada vuelta del ciclo |
# | diferencia | int | Distancia absoluta entre el intento y el número secreto | En cada vuelta del ciclo |
# 

# %% [markdown]
# ## 8. Código del estudiante
# 
# Escriba aquí su solución completa.
# 

# %%
# Escriba aquí su juego Adivina el número.

import random

print("🎯 ADIVINA EL NUMERO SECRETO 🎯")
print("REGLAS \n1-Ingrese solamente numeros del 1 al 20\n2-Solo se pueden usar numeros, no ingrese letras")

numero_secreto = random.randint(1, 20)
intentos = 0


while True:
    entrada = input("Escriba un número del 1 al 20: ").strip()
    
    if not entrada:
        continue

    try:
        numero = int(entrada)
    except ValueError:
        print("Solo se permiten números, no letras. Intente de nuevo.")
        continu

    if numero < 1 or numero > 20:
        print("El número debe estar entre 1 y 20. Intente de nuevo.")
        continue

    intentos += 1
    numero = int(entrada)
    diferencia = abs(numero_secreto - numero)

    if diferencia == 0:
        print(f"🎉 Felicidades!\nAdivinaste el numero secreto {numero_secreto} en {intentos} intentos")
        break
    elif diferencia in range(1, 3):
        print(f"Intento {intentos}: Hirviendo, está casi encima del número.")
    elif diferencia in range(3, 6):
        print(f"Intento {intentos}: Caliente, está cerca.")
    elif diferencia in range(6, 11):
        print(f"Intento {intentos}: Tibio, va por buen camino pero falta.")
    else:
        print(f"Intento {intentos}: Frío, está lejos.")

    if numero_secreto > numero:
        print("El numero secreto es MAYOR\n")
    elif numero_secreto < numero:
        print("El numero secreto es MENOR\n")
        
    
        
             
        
      


# %% [markdown]
# ## 9. Evidencia de pruebas
# 
# Registre tres ejecuciones manuales. Puede copiar la salida de la consola o
# describir exactamente qué escribió y qué respondió el programa.
# 
# | Prueba | Intentos realizados | Pistas de dirección y temperatura | Resultado observado |
# |---|---|---|---|
# | Intento frío | 1 intento: número=2, secreto=17 | Frío, está lejos." / El número secreto es MAYOR | El programa mostró la pista de temperatura y la dirección correctamente |
# | Intento caliente o hirviendo | 3 intentos: 10 → tibio/MAYOR, 15 → caliente/MAYOR, 16 → hirviendo/MAYOR | Pistas de temperatura y dirección en cada intento | Las pistas guiaron al usuario progresivamente hacia el número |
# | Intento correcto | 4 intentos: llegando al número secreto 17 | Último intento sin pista de dirección, solo mensaje de victoria | "🎉 Felicidades! Adivinaste el numero secreto 17 en 4 intentos" |
# 

# %% [markdown]
# ## 10. Reflexión
# 
# Responda con dos o tres oraciones:
# 
# 1. ¿Por qué este programa necesita repetir instrucciones?
# Porque no se sabe de antemano cuántos intentos necesitará el usuario para acertar, por lo que el ciclo while True mantiene el juego activo hasta que se cumpla la condición de salida.
# 2. ¿Dónde termina el ciclo y por qué?
# Termina cuando diferencia == 0, es decir, cuando el intento coincide exactamente con el número secreto; en ese momento se ejecuta break y el ciclo se detiene.
# 3. ¿Cómo usó la distancia para decidir si el intento estaba frío, tibio, caliente o hirviendo?
# Se calculó con abs(numero_secreto - numero) para obtener siempre un valor positivo, y luego se evaluó ese valor con elif para asignar la pista correspondiente: hirviendo si la distancia es 1 o 2, caliente entre 3 y 5, tibio entre 6 y 10, y frío si supera 10.
# 


