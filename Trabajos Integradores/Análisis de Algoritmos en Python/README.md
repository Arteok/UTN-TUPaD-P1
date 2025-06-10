# Comparación de Algoritmos para Detección de Palíndromos

Este proyecto implementa y compara dos algoritmos para verificar si una palabra o frase es un palíndromo. Se evalúa su eficiencia mediante experimentación con listas de entrada de tamaño creciente.

## Descripción

Se desarrollaron dos funciones que determinan si una palabra es un palíndromo:

**Algoritmo Recursivo:** Compara los extremos de la cadena y llama a sí mismo con la subcadena restante.
**Algoritmo con Slicing:** Utiliza slicing inverso (`[::-1]`) para comparar la palabra con su reverso.

Se mide el tiempo de ejecución de ambos algoritmos a medida que crece el tamaño de la lista de palabras. Los resultados muestran cómo la eficiencia varía según la implementación.

## Estructura del experimento

**Lista base:** 20 palabras (10 palíndromos + 10 no palíndromos).
- En cada iteración se duplica el tamaño de la lista hasta alcanzar 10 veces el tamaño inicial.
- Se mide el tiempo total de ejecución de cada algoritmo para la lista en cada iteración.
- Se imprime la diferencia absoluta y relativa entre los dos métodos.
