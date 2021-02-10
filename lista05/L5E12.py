# Feito por Vinícius Silva Sena
#12
import random

def embaralhar(palavra):
  n = list(palavra)
  random.shuffle(n)
  result = ''.join(n)
  return result.lower()

palavra = input("Informe uma palavra: ")
print(embaralhar(palavra))
