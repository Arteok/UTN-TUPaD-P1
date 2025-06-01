import random
import time
import bisect

# O(1): Accede al primer elemento de la lista
def operacion_constante(lista):
    return lista[0]

# O(log n): Búsqueda binaria en una lista ordenada
def operacion_logaritmica(lista, valor):
    lista_ordenada = sorted(lista)  # Primero ordenamos la lista
    return bisect.bisect_left(lista_ordenada, valor)  # Búsqueda binaria

# O(n): Suma de todos los elementos
def operacion_lineal(lista):
    return sum(lista)

# O(n log n): Ordenamiento de la lista
def operacion_nlogn(lista):
    return sorted(lista)

# O(n²): Comparación de cada elemento con todos los demás (doble bucle)
def operacion_cuadratica(lista):
    conteo = 0
    for i in lista:
        for j in lista:
            if i == j:
                conteo += 1
    return conteo

if __name__ == "__main__":
    try:
        # Pedimos al usuario cuántos números aleatorios quiere generar
        n = int(input("Ingrese la cantidad de números aleatorios a generar: "))
        if n <= 0:
            raise ValueError

        # Generamos una lista de n números aleatorios entre 1 y 10.000
        lista = [random.randint(1, 10000) for _ in range(n)]
        valor_busqueda = random.choice(lista)  # Tomamos un valor aleatorio de la lista para buscar

        print("\n📊 Medición de tiempos por complejidad:")

        # O(1) - Tiempo constante
        inicio = time.time()
        operacion_constante(lista)
        print(f"O(1)        - Operación constante:       {time.time() - inicio:.8f} segundos")

        # O(log n) - Búsqueda binaria
        inicio = time.time()
        operacion_logaritmica(lista, valor_busqueda)
        print(f"O(log n)    - Búsqueda binaria:          {time.time() - inicio:.8f} segundos")

        # O(n) - Suma de todos los elementos
        inicio = time.time()
        operacion_lineal(lista)
        print(f"O(n)        - Suma de elementos:         {time.time() - inicio:.8f} segundos")

        # O(n log n) - Ordenamiento
        inicio = time.time()
        operacion_nlogn(lista)
        print(f"O(n log n)  - Ordenamiento:              {time.time() - inicio:.8f} segundos")

        # O(n²) - Comparación de todos contra todos, solo si n es menor o igual a 1000
        if n <= 1000:
            inicio = time.time()
            operacion_cuadratica(lista)
            print(f"O(n²)       - Comparación doble bucle:   {time.time() - inicio:.8f} segundos")
        else:
            print("O(n²)       - Saltado por tamaño (n > 1000)")

    except ValueError:
        print("Por favor ingrese un número entero positivo.")
