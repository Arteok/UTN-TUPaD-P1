# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def mystery(n):
    if n <= 1:
        return n
    else:
        return mystery(n - 1) + mystery(n - 2)
    
print(mystery(4))