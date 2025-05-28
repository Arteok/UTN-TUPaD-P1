# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicitar peso y altura al usuario

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

if altura <= 0:
    print("La altura debe ser mayor que cero.")
else:
    imc = calcular_imc(peso, altura)
    print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")






