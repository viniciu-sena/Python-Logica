# Feito por Vinícius Silva Sena
#23
n = int(input("Informe o numero de valores: "))
primos = []
valores = []
divisoes = 0

for i in range(n):
  cont = 0
  for x in range(i):
    divisoes += 1
    if (i % (x+1)) == 0:
      cont += 1
  if cont == 2:
    primos.append(i)

for i in range(len(primos)):
  print("Primo: ",primos[i])
print("Divisões: ",divisoes)
print("Numero de primos: ",len(primos))
