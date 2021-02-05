#17

ano = int(input("Digite um ano: "))

resto = ano % 4

if (resto == 0):
  print(ano,"É um ano bissexto")
else:
  print(ano,"Não é um ano bissexto")
