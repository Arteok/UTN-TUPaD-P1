
def repetir_frase(num, frase):
    if num > 0:
        print(frase)
        repetir_frase(num - 1, frase)
