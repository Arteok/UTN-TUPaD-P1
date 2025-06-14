from itertools import product
from collections import Counter
from datetime import datetime

# --- Funciones de colores para consola ---

# Devuelve el código ANSI del color para usar en la terminal
def obtener_color(codigo_color):
    colores = {
        "cyan": "\033[96m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "reset": "\033[0m"
    }
    return colores.get(codigo_color, colores["reset"])

# Envuelve un texto con un color ANSI
def color(texto, codigo_color):
    return obtener_color(codigo_color) + texto + obtener_color("reset")

# --- Funciones para entrada de datos ---

# Devuelve diccionarios con datos predefinidos de nombres, DNIs y años
def cargar_datos_predefinidos():
    dnis = {
        "Pablo": "31760481",
        "Francisco": "45933343",
        "El Loco Blanco": "28807112"
    }
    anios = {
        "Pablo": 1985,
        "Francisco": 2005,
        "El Loco Blanco": 1980
    }
    return dnis, anios

# Pide el DNI de una persona y valida que solo tenga números
def pedir_dni(nombre):
    while True:
        dni = input(f"Ingrese el DNI de {nombre} (sin puntos): ")
        if dni.isdigit():
            return dni
        print(color("DNI inválido. Ingrese solo números.", "yellow"))

# Pide el año de nacimiento y valida que sea un número
def pedir_anio(nombre):
    while True:
        anio = input(f"Ingrese el año de nacimiento de {nombre}: ")
        if anio.isdigit():
            return int(anio)
        print(color("Año inválido. Ingrese un número válido.", "yellow"))

# Permite ingresar datos manualmente de 4 personas
def cargar_datos_manual(cantidad=4):
    dnis = {}
    anios = {}
    for i in range(1, cantidad + 1):
        nombre = input(f"Ingrese el nombre de la persona {i}: ")
        dni = pedir_dni(nombre)
        anio = pedir_anio(nombre)
        dnis[nombre] = dni
        anios[nombre] = anio
    return dnis, anios

# --- Funciones para dígitos únicos ---

# Convierte cada DNI a un conjunto de dígitos únicos
def obtener_conjuntos_digitos(dnis):
    return {k: set(map(int, v)) for k, v in dnis.items()}

# Imprime los conjuntos de dígitos únicos por persona
def imprimir_conjuntos_digitos(conjuntos):
    print(color("\nConjuntos de dígitos únicos:", "green"))
    for persona, conjunto in conjuntos.items():
        print(f"{persona}: {conjunto}")

# Realiza operaciones de conjuntos entre las dos primeras personas
def imprimir_operaciones_conjuntos(conjuntos):
    nombres = list(conjuntos.keys())
    if len(nombres) < 2:
        return
    a, b = nombres[0], nombres[1]
    print(color(f"\nOperaciones entre conjuntos ({a} y {b}):", "green"))
    print(f"Unión ({a} ∪ {b}): {conjuntos[a] | conjuntos[b]}")
    print(f"Intersección ({a} ∩ {b}): {conjuntos[a] & conjuntos[b]}")
    print(f"Diferencia ({a} - {b}): {conjuntos[a] - conjuntos[b]}")
    print(f"Diferencia simétrica ({a} Δ {b}): {conjuntos[a] ^ conjuntos[b]}")

# Muestra la frecuencia de cada dígito en cada DNI y su suma total
def imprimir_frecuencia_suma(dnis):
    print(color("\nFrecuencia y suma de dígitos:", "green"))
    for persona, dni in dnis.items():
        print(f"{persona}: DNI = {dni}")
        frecuencia = Counter(dni)
        suma = sum(int(d) for d in dni)
        print(f"Frecuencia: {dict(frecuencia)}, Suma: {suma}\n")

# Detecta personas con tendencia a usar dígitos bajos (<3)
def hay_tendencia_digitos_bajos(conjuntos):
    return [(k, v) for k, v in conjuntos.items() if any(d < 3 for d in v)]

# Detecta pares de personas cuyos conjuntos no comparten ningún dígito
def hay_conjuntos_completamente_diferentes(conjuntos):
    claves = list(conjuntos.keys())
    resultados = []
    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):
            c1, c2 = claves[i], claves[j]
            if conjuntos[c1].isdisjoint(conjuntos[c2]):
                resultados.append((c1, c2))
    return resultados

# Evalúa condiciones lógicas sobre los conjuntos de dígitos
def imprimir_condiciones_logicas(conjuntos):
    print(color("\nEvaluación de condiciones lógicas:", "green"))

    tendencia = hay_tendencia_digitos_bajos(conjuntos)
    if len(tendencia) >= 2:
        print("→ Grupo con tendencia a dígitos bajos (dígitos < 3):")
        for nombre, conjunto in tendencia:
            print(f"  {nombre}: {conjunto}")
    else:
        print("→ No hay suficiente tendencia a dígitos bajos.")

    disjuntos = hay_conjuntos_completamente_diferentes(conjuntos)
    if disjuntos:
        print("→ Hay conjuntos completamente diferentes:")
        for par in disjuntos:
            print(f"  {par[0]} y {par[1]}")
    else:
        print("→ No hay conjuntos completamente diferentes.")

# Separa las personas en las que nacieron en años pares e impares
def contar_pares_impares(anios):
    pares = [nombre for nombre, anio in anios.items() if anio % 2 == 0]
    impares = [nombre for nombre in anios if nombre not in pares]
    return pares, impares

# Muestra análisis de los años de nacimiento
def imprimir_analisis_anios(anios):
    print(color("\nAnálisis de años de nacimiento:", "green"))
    pares, impares = contar_pares_impares(anios)
    print(f"Pares ({len(pares)}): {', '.join(pares)}")
    print(f"Impares ({len(impares)}): {', '.join(impares)}")

# Indica si un año es bisiesto
def es_bisiesto(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)

# Verifica si algún año de nacimiento es bisiesto
def hay_anio_bisiesto(anios):
    return any(es_bisiesto(a) for a in anios.values())

# Imprime a qué generación pertenece el grupo
def imprimir_generacion(anios):
    print(color("\nGeneración:", "green"))
    if all(a > 2000 for a in anios.values()):
        print("→ Grupo Z")
    else:
        print("–")

# Imprime si existe un año bisiesto en el grupo
def imprimir_anios_bisiestos(anios):
    print(color("\nAño bisiesto:", "green"))
    if hay_anio_bisiesto(anios):
        print("→ Tenemos un año especial")
    else:
        print("–")

# Calcula las edades a partir del año actual
def calcular_edades(anios):
    actual = datetime.now().year
    return {k: actual - v for k, v in anios.items()}

# Muestra el producto cartesiano entre años de nacimiento y edades
def imprimir_producto_cartesiano(anios, edades):
    conjunto_anios = set(anios.values())
    conjunto_edades = set(edades.values())
    producto = list(product(conjunto_anios, conjunto_edades))
    print(color("\nProducto cartesiano (año, edad):", "green"))
    for par in producto:
        print(par)

# --- Función general que ejecuta todos los análisis ---
def analizar_datos(dnis, anios):
    conjuntos = obtener_conjuntos_digitos(dnis)
    imprimir_conjuntos_digitos(conjuntos)
    imprimir_operaciones_conjuntos(conjuntos)
    imprimir_frecuencia_suma(dnis)
    imprimir_condiciones_logicas(conjuntos)
    imprimir_analisis_anios(anios)
    imprimir_generacion(anios)
    imprimir_anios_bisiestos(anios)
    edades = calcular_edades(anios)
    imprimir_producto_cartesiano(anios, edades)

# --- Menú de usuario ---

# Muestra las opciones del menú principal
def mostrar_menu():
    print(color("\n====== MENÚ PRINCIPAL ======", "cyan"))
    print("1. Usar los DNIs predefinidos")
    print("2. Cargar 4 DNIs manualmente")
    print("3. Salir")

# Pide una opción del menú
def pedir_opcion():
    return input("Seleccione una opción (1-3): ")

# --- Función principal del programa ---
def main():
    seguirEnElMenu = True #Para no tener que usar break
    while seguirEnElMenu == True:
        mostrar_menu()
        opcion = pedir_opcion()
        if opcion == "1":
            dnis, anios = cargar_datos_predefinidos()
            analizar_datos(dnis, anios)
        elif opcion == "2":
            dnis, anios = cargar_datos_manual(4)
            analizar_datos(dnis, anios)
        elif opcion == "3":
            print(color("Saliendo del programa...", "red"))
            seguirEnElMenu = False
        else:
            print(color("Opción inválida. Intente de nuevo.\n", "yellow"))

# Llama a main solo si el script es ejecutado directamente
if __name__ == "__main__":
    main()
