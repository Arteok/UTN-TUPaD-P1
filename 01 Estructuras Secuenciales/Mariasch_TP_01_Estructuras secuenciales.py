# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
# Imprimir la información en una oración
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
# Pedir el radio al usuario
radio = float(input("Ingresa el radio del círculo: "))
# Calcular el área y el perímetro
pi = float(3.14)
area = pi * radio ** 2
perimetro = 2 * pi * radio
# Imprimir los resultados
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla acuántas horas equivale.
# Pedir al usuario una cantidad de segundos
segundos = int(input("Ingrese la cantidad de segundos: "))
# Convertir a horas
horas = segundos / 3600
# Imprimir el resultado
print(f"{segundos} segundos equivalen a {horas} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar de {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
# Pedir al usuario dos números enteros distintos de 0
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
# Realizar las operaciones y mostrar los resultados
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 
# Imprimir los resultados
print(f"Resultados:")
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Pedir al usuario su altura en metros y peso en kilogramos
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
# Calcular el Índice de Masa Corporal (IMC)
imc = peso / (altura ** 2)
# Imprimir el resultado
print(f"Su Índice de Masa Corporal (IMC) es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Solicitar la temperatura en grados Celsius al usuario
celsius = float(input("Introduce la temperatura en grados Celsius: "))
# Convertir la temperatura a Fahrenheit
fahrenheit = (9/5) * celsius + 32
# Imprimir el resultado
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}°F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
# Solicitar tres números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))
# Calcular el promedio
promedio = (numero1 + numero2 + numero3) / 3
# Imprimir el promedio
print(f"El promedio de los tres números es: {promedio}")
