# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_OwFJ5weOGWy41GZzMJLvkS6Ni1amWfv
"""

temperatura = int(input("Qual a temperatura atual? ")) # Pede a temperatura atual
if temperatura > 30:
  print("Está quente.") # Se a temperatura for maior que 30, imprime a mensagem que está quente.
elif temperatura < 15:
  print("Está frio.")  # Se a temperatura for menor que 30, imprime a mensagem que está quente.
else:
  print("Está agradável.")  # Se não atender as duas primeiras, a temperatura será agradável