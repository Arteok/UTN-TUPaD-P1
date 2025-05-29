# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        cuenta_actual = 1 if (numero % 10) == digito else 0
        return cuenta_actual + contar_digito(numero // 10, digito)

# Solicitar al usuario los datos
numero = int(input("Introduce un número entero positivo: "))
digito = int(input("Introduce el dígito que deseas contar (0-9): "))

resultado = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
