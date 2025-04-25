#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Pedimos al usuario que ingrese una frase o palabra
frase = input("Por favor, ingrese una frase o palabra: ")

# Para acceder a la última letra de un string podemos usar el índice -1
# Si la última letra de la frase (frase[-1]) es una vocal, agregar un signo
# de exclamación e imprimirla
if frase[-1] in ("AEIOUaeiou"):
  print(f"{frase}!")
# Sino, imprimir la frase tal cual fue ingresada
else:
  print(frase)