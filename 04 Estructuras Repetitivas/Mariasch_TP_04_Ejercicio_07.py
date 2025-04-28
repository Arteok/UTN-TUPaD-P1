#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# Solicitamos al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Inicializamos la variable suma en 0
suma = 0

# Usamos un bucle for para sumar todos los números desde 0 hasta n
for i in range(n + 1):  
    suma += i

# Mostramos el resultado de la suma
print(f"La suma de todos los números entre 0 y {n} es: {suma}")
