import random
import time
from itertools import permutations

# O(1): Accede al primer elemento
def operacion_constante(lista):
    inicio_tiempo = time.time()
    resultado = lista[0]  # Operación O(1)
    fin_tiempo = time.time()
    
    return resultado, fin_tiempo - inicio_tiempo 

# Ordenar la lista solo para usar en lista binaria
def ordenar_lista_binaria(lista):
    return sorted(lista) 

# O(log n): Búsqueda binaria con medición de tiempo
def operacion_logaritmica(lista_ordenada, valor):
    inicio_tiempo = time.time()  # Comienza a medir tiempo

    inicio = 0
    fin = len(lista_ordenada) - 1

    while inicio <= fin:  # BIG O: O(log n)
        medio = (inicio + fin) // 2
        if lista_ordenada[medio] == valor:
            fin_tiempo = time.time()                                  
            return medio, fin_tiempo - inicio_tiempo # Resultado + tiempo
        
        elif lista_ordenada[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1

    fin_tiempo = time.time()
    return -1, fin_tiempo - inicio_tiempo   # Si no lo encuentra, -1 y tiempo

# O(n): Suma de elementos con medición de tiempo
def operacion_lineal(lista):
    inicio_tiempo = time.time()  

    total = 0
    for numero in lista:  # BIG O: O(n)
        total += numero

    fin_tiempo = time.time()  

    return total, fin_tiempo - inicio_tiempo 

# O(n log n): Ordenamiento con Merge Sort, todo dentro de una sola función
def operacion_nlogn(lista):
    
    # Función interna recursiva que aplica el algoritmo Merge Sort
    def merge_sort(sublista):
        if len(sublista) <= 1:
            return sublista
                
        medio = len(sublista) // 2
        izquierda = merge_sort(sublista[:medio])   
        derecha = merge_sort(sublista[medio:])  
                
        return merge(izquierda, derecha)

    # Función que fusiona dos listas ordenadas en una sola ordenada
    def merge(izquierda, derecha):
        resultado = []
        i = j = 0

        # Recorremos ambas listas y comparamos elementos
        while i < len(izquierda) and j < len(derecha): # Big O: O(n log n)
            if izquierda[i] < derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        # Agregamos los elementos restantes si quedaron
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

    # Medición del tiempo de ejecución
    inicio_tiempo = time.time()
    resultado_ordenado = merge_sort(lista)  # Aquí ocurre el ordenamiento completo
    fin_tiempo = time.time()

    # Devolvemos la lista ordenada y el tiempo que tardó
    return resultado_ordenado, fin_tiempo - inicio_tiempo 


# O(n²): Comparación doble bucle (fuerza bruta)
def operacion_cuadratica(lista):
    inicio_tiempo = time.time()  

    conteo = 0
    for i in lista:
        for j in lista:
            if i == j:
                conteo += 1
    # ↑ Estas dos líneas combinadas (doble bucle) generan una complejidad O(n²)

    fin_tiempo = time.time() 

    return conteo, fin_tiempo - inicio_tiempo  

# O(2ⁿ): Fibonacci recursivo
def operacion_exponencial(n):
    if n <= 1:
        return n
    return operacion_exponencial(n - 1) + operacion_exponencial(n - 2)

# O(n!): Generación de permutaciones
def operacion_factorial(lista):
    return list(permutations(lista))

if __name__ == "__main__":
    try:
        # Pedir cantidad de números aleatorios
        print("Órdenes de Complejidad - BIG - O")
        n = int(input("Ingrese la cantidad de números aleatorios a generar(no mas de 35 please): "))
        if n <= 0:
            raise ValueError # Dispara manualmente el error porque fue menor a 0 la cantidad ingresada

        lista = [random.randint(10, 100) for _ in range(n)]
        
        print("Medición de tiempos por complejidad: ")

        # O(1)       
        valor_constante, tiempo_constante = operacion_constante(lista)
        print(f"Constante - EL primer elemento de la lista es: {valor_constante}")
        print(f"O(1)        - Operación constante:       {tiempo_constante:.8f} segundos")        

        # O(log n)
        lista_binaria = ordenar_lista_binaria(lista)
        valor_logaritmica, tiempo_logaritmica = operacion_logaritmica(lista_binaria, valor_constante)
        print(f"Logarítmica - Se busca el elemento seleccionado en la funcion anterior ({valor_constante}) y lo encontro en la posición numero {valor_logaritmica} de la lista despues de ser ordenada.")
        print(f"O(log n)    - Búsqueda binaria:          {tiempo_logaritmica:.8f} segundos")

        # O(n)
        valor_lineal, tiempo_lineal = operacion_lineal(lista)
        print(f"Lineal - Se suman todos los elementos de la lista y el valor resultante es: {valor_lineal}.")
        print(f"O(n)        - Suma de elementos:         {tiempo_lineal:.8f} segundos")

        # O(n log n)
        lista_ordenada_nlogn, tiempo_nlogn = operacion_nlogn(lista)
        print(f"N log N -📋 Lista ordenada: {lista_ordenada_nlogn}")
        print(f"O(n log n)  - Ordenamiento:              {tiempo_nlogn:.8f} segundos")

        # O(n²)
        valor_cuadratica, tiempo_cuadratica = operacion_cuadratica(lista)
        print(f"Cuadratica - Cantidad de comparaciones positivas: {valor_cuadratica}")
        print(f"O(n²)       - Comparación doble bucle:   {tiempo_cuadratica:.8f} segundos")        

        # O(2ⁿ)  
        inicio = time.time()
        if lista_ordenada_nlogn[0] <= 35:
            resultado_exponencial = operacion_exponencial(lista_ordenada_nlogn[0])
            print(f"Fibonacci de {lista_ordenada_nlogn[0]}: {resultado_exponencial}")
            print(f"O(2ⁿ)       - Fibonacci recursivo: {time.time() - inicio:.8f} segundos") 
        else:
            print(f"El primer numero de la lista es {lista_ordenada_nlogn[0]} y es demaciado grande.")

            
        # O(n!)
        """ if n <= 100:
            inicio = time.time()
            operacion_factorial(lista[:n])
            print(f"O(n!)       - Permutaciones (n={n}):      {time.time() - inicio:.8f} segundos")
        else:
            print("O(n!)       - Saltado por tamaño (n > 100)") """

    except ValueError:
        print("Por favor ingrese un número entero positivo.")
