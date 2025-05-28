# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

# Solicitar los segundos al usuario

segundos = float(input("Ingresa la cantidad de segundos: "))

horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")


