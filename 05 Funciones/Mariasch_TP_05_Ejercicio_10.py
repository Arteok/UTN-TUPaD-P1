#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

# Creamos la lista anidada con los valores indicados
lista_anidada = [
    15,                 # lista_anidada[0]
    True,               # lista_anidada[1]
    [25.5, 57.9, 30.6], # lista_anidada[2][0], [2][1], [2][2]
    False               # lista_anidada[3]
]

# Imprimimos la lista resultante
print("Lista anidada:", lista_anidada)
