def eh_primo(numero):
  if numero <=1:
    return False
  for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
      return False
  return True

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print("Números primos no intervalo de", inicio, "a", fim, "são:")
for numero in range(inicio, fim + 1):
  if eh_primo(numero):
    print(numero, end=" ")

