# Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar un número al usuario
numero = int(input("Introduce un número entero positivo: "))

binario = decimal_a_binario(numero)
print(f"{numero} en binario es: {binario}")
