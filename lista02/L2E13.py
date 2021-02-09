# Feito por Vinícius Silva Sena
#13
import numpy as np
semana = ["domingo","segunda","terca","quarta","quinta","sexta","sabado"]
dia = int(input("informe o dia da semana: "))

try:
  if dia <= 0:
    print("Valor invalido")
  else:
    print(semana[dia-1])
except:
  print("Valor invalido")
