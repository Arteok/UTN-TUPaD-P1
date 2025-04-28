#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random  # Para generar números aleatorios

# Generamos un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)

# Inicializamos el contador de intentos y una bandera 'adivinó' en False
intentos = 0
adivino = False

# Iniciamos el bucle while que continuará hasta que el usuario adivine el número
while not adivino:
    # Pedimos al usuario que ingrese su intento
    intento_usuario = int(input("Adivina un número entre 0 y 9: "))
    
    # Incrementamos el contador de intentos
    intentos += 1
    
    # Verificamos si el intento es correcto
    if intento_usuario == numero_aleatorio:
        adivino = True  
        print(f"Felicidades! Adivinaste el número en {intentos} intentos.")
    else:
        print("Número incorrecto, intenta de nuevo.")

