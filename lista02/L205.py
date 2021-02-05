#05

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print("Média: %.2f" % media)

if (media >= 7):
  if (media == 10):
    print("Aprovado com Distinção!")
  else:
    print("Aprovado!")

elif (media < 7):
  print("Reprovado!")
