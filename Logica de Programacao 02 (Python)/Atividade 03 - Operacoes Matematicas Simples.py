# Pede dois números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Calcula as operações
soma = num1 + num2 # Soma
subtracao = num1 - num2 # Subtração
multiplicacao = num1 * num2 # Multiplicação
divisao = num1 / num2 if num2 != 0 else "Nenhum número pode ser didivido por zero" # Divisão

# Resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
