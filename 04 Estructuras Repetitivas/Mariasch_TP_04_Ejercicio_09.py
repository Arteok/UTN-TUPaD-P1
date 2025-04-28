#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule lamedia de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

# Definimos la cantidad de números a ingresar
CANTIDAD_NUMEROS = 10  #Al cambiar CANTIDAD_NUMEROS a 100, el programa cumple la consigna sin alterar su lógica.

# Inicializamos la suma
suma = 0

# Pedimos los números y los vamos sumando
for _ in range(CANTIDAD_NUMEROS):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

# Calculamos la media
media = suma / CANTIDAD_NUMEROS

# Mostramos el resultado
print(f"La media de los {CANTIDAD_NUMEROS} números ingresados es: {media}")
