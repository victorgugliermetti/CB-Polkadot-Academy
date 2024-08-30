def count_a(frase):
    contador = 0
    for letra in frase:
        if letra == 'a':
            contador += 1
    return contador

frase = input("Digite uma frase: ")
resultado = count_a(frase)
print("O número de vezes que a letra a aparece na frase é:", resultado)
