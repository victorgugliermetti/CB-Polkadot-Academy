temperatura = int(input("Qual a temperatura atual? ")) # Pede a temperatura atual
if temperatura > 30:
  print("Está quente.") # Se a temperatura for maior que 30, imprime a mensagem que está quente.
elif temperatura < 15:
  print("Está frio.")  # Se a temperatura for menor que 30, imprime a mensagem que está quente.
else:
  print("Está agradável.")  # Se não atender as duas primeiras, a temperatura será agradável
