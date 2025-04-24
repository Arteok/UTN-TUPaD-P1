#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# Solicita la nota al usuario y la convierte a número
nota = int(input("Ingrese su nota: "))

# Evalúa si la nota es suficiente para aprobar
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
