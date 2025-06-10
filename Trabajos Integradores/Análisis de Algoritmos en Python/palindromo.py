import time

# Funciones de verificación de palíndromos

# Algoritmo 1: Recursivo
def es_palindromo_recursiva(palabra):
    palabra = palabra.lower().replace(" ", "")
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo_recursiva(palabra[1:-1]) # Big O = n²

# Algoritmo 2: Slicing
def es_palindromo_slice(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1] #Big  O = n

# Función para medir tiempos
def medir_tiempos(funcion, palabras):
    inicio = time.time()  # Mayor precisión
    for palabra in palabras:
        funcion(palabra)
    fin = time.time()
    return fin - inicio

# Lista base de palabras (10 palíndromos + 10 no palíndromos)
palabras_base = [
    # Palíndromos
    "Reconocer", "Anita lava la tina", "A man a plan a canal Panama", 
    "oso", "arenera", "Salas", "Somos", "Rayar", "Rotator", "Neuquén",
    # No palíndromos
    "Python", "Computadora", "Algoritmo", "Programación", "OpenAI",
    "JavaScript", "Bucle", "Función", "Variable", "String"
]

# Experimentación con tamaño creciente
print("================        Crecimiento del tiempo vs tamaño de lista (n)         ================")
print("n\tTiempo Recursivo\tTiempo Slicing\t\tDiferencia (s)\t\tDiferencia (%)")

n_inicial = 20  # Empezamos con las 20 palabras base
for i in range(1, 11):  # 10 iteraciones
    n = n_inicial * (2 ** (i - 1))  # Duplicamos n en cada iteración
    palabras = palabras_base * (n // 20 + 1)  # Extendemos la lista
    palabras = palabras[:n]  # Aseguramos tamaño exacto
    
    # Medición
    tiempo_rec = medir_tiempos(es_palindromo_recursiva, palabras)
    tiempo_slice = medir_tiempos(es_palindromo_slice, palabras)
    
    # Cálculo de diferencia absoluta y relativa
    diferencia_segundos = tiempo_rec - tiempo_slice
    try:
        diferencia_porcentaje = (diferencia_segundos / tiempo_slice) * 100
    except ZeroDivisionError:
        diferencia_porcentaje = 0.0  # Evita división por cero si tiempo_slice es cero
    
    # Resultados
    print(f"{n}\t   {tiempo_rec:.6f} s\t\t  {tiempo_slice:.6f} s\t\t  {diferencia_segundos:.6f} s\t\t   {diferencia_porcentaje:.2f} %")
