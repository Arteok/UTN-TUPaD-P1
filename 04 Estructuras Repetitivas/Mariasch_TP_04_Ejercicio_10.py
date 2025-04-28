#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Pedimos al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

numero_invertido = 0

while numero > 0:
    digito = numero % 10  # Último dígito
    numero_invertido = numero_invertido * 10 + digito  # Agregamos el dígito
    numero = numero // 10  # Quitamos el último dígito

# Mostramos el resultado
print(f"El número invertido es: {numero_invertido}")
