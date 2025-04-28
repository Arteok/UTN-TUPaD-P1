#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Tomamos el valor absoluto para ignorar el signo
numero_abs = abs(numero)

# Convertimos el número a cadena y contamos los caracteres
cantidad_digitos = len(str(numero_abs))

# Mostramos el resultado
print(f"El número tiene {cantidad_digitos} dígitos.")
