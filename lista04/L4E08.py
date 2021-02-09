# Feito por Kelvin Schneider
#08

idade = []
altura = []

i = 0
while (i < 5):
  tec = int(input("Digite sua idade: "))
  idade.append(tec)

  tec = float(input("Digite sua altura [1.70]: "))
  altura.append(tec)

  i+=1

print("\n------------ idade -------------- \n")

for i in reversed(idade):
  print(i)

print("\n------------ altura ------------- \n")

for i in reversed(altura):
  print(i)
