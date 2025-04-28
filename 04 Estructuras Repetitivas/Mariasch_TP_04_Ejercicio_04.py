#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# Inicializamos la suma y la variable 'numero' con un valor distinto de 0
suma_total = 0
numero = 1

# Usamos un bucle while con condición que verifique si el número es diferente de 0
while numero != 0:
    # Solicitamos un número al usuario
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    
    # Si el número no es 0, lo sumamos
    if numero != 0:
        suma_total += numero

# Mostramos el total
print(f"La suma total de los números ingresados es: {suma_total}")
