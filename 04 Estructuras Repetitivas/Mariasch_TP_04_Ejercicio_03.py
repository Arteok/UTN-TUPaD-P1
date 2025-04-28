#Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# Solicitamos los dos números al usuario
inicio = int(input("Ingrese el primer número entero: "))
fin = int(input("Ingrese el segundo número entero: "))

# Si el primer número es mayor que el segundo, los intercambiamos
if inicio > fin:
    inicio, fin = fin, inicio

# Inicializamos la suma en 0
suma = 0

# Usamos un bucle for para recorrer los números entre 'inicio' y 'fin'
for i in range(inicio + 1, fin):
    if i % 2 == 0: # Verificar si el número es par
        suma += i  

# Mostramos el resultado
print(f"La suma de los números enteros entre {inicio} y {fin} (excluyéndolos) es: {suma}") 
