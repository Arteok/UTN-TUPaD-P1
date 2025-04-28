#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Definimos la cantidad de números a ingresar
CANTIDAD_NUMEROS = 10  #Al cambiar CANTIDAD_NUMEROS a 100, el programa cumple la consigna sin alterar su lógica.

# Inicializamos contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Bucle para ingresar los números
for _ in range(CANTIDAD_NUMEROS):
    numero = int(input("Ingrese un número entero: "))
    
    # Verificamos si es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Verificamos si es positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    # Si es 0 no sumamos ni a positivos ni a negativos

# Mostramos los resultados
print("\nResultados:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
