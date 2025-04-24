#El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.


import random
from statistics import mode, median, mean

# Genera la lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcula media, mediana y moda
media_valor = mean(numeros_aleatorios)
mediana_valor = median(numeros_aleatorios)
moda_valor = mode(numeros_aleatorios)

# Muestra los valores calculados
print(f"Media: {media_valor}")
print(f"Mediana: {mediana_valor}")
print(f"Moda: {moda_valor}")

# Determina el sesgo
if media_valor > mediana_valor > moda_valor:
    print("Sesgo positivo (a la derecha)")
elif media_valor < mediana_valor < moda_valor:
    print("Sesgo negativo (a la izquierda)")
elif media_valor == mediana_valor == moda_valor:
    print("Sin sesgo")
else:
    print("No cumple con ningún sesgo específico")

