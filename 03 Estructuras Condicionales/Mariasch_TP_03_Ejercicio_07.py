#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Solicitar frase o palabra al usuario
texto = input("Ingrese una frase o palabra: ")

# Verificar si el string termina con vocal
if len(texto) > 0:
    ultimo_caracter = texto[-1].lower()
    if (ultimo_caracter == 'a' or ultimo_caracter == 'e' or 
        ultimo_caracter == 'i' or ultimo_caracter == 'o' or 
        ultimo_caracter == 'u' or ultimo_caracter == 'á' or
        ultimo_caracter == 'é' or ultimo_caracter == 'í' or
        ultimo_caracter == 'ó' or ultimo_caracter == 'ú'):
        texto += "!"
# Imprimir el resultado
print(texto)
