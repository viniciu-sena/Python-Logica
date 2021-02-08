#20
import math

n = int(input("N° de valores: "))
valores = []
i = 0

while i < n:
  valor = int(input("informe o valor: "))
  if valor >= 1 and valor <= 16:
    valores.append(valor)
    i += 1

for i in range(len(valores)):
  print("Fatorial de ",valores[i]," é: ",math.factorial(valores[i]))
