# Feito por Kelvin Schneider
#02

num = int(input("Digite um numero: "))

def criarLinha(num):
  for i in range(1, num + 1):
    print((" {} ").format(i), end="")

  print("")

def imprimir(num):
  for num in range(num + 1):
    criarLinha(num)

imprimir(num)
