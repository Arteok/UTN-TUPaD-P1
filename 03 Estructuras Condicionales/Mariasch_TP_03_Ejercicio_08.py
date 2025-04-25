#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Solicitar al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Mostrar las opciones disponibles
print("\nOpciones de formato:")
print("1. Nombre en MAYÚSCULAS")
print("2. nombre en minúsculas")
print("3. Nombre con primera letra mayúscula")

# Solicitar la opción deseada
opcion = input("\nElija una opción (1, 2 o 3): ")

# Transformar el nombre según la opción seleccionada
if opcion == "1":
    nombre_transformado = nombre.upper()
elif opcion == "2":
    nombre_transformado = nombre.lower()
elif opcion == "3":
    nombre_transformado = nombre.title()
else:
    nombre_transformado = "Opción no válida. Debe ingresar 1, 2 o 3."

# Mostrar el resultado
print("\nResultado:", nombre_transformado)