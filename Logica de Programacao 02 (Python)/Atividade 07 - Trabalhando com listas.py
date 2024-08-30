lista_de_compras = []

while True:
    item = input("Digite um item para adicionar a lista de compras (ou digite fim para terminar): ")
    if item == "fim":
        break
    lista_de_compras.append(item)

print("\nSua lista de compras:")
for item in lista_de_compras:
    print(item)
