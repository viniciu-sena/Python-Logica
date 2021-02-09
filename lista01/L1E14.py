# Feito por Vinícius Silva Sena
#14
peso = float(input("Digite o peso dos peixes: "))

if (peso > 50):
  excesso = peso - 50
  multa = excesso * 4
  print("Peso dos paixes teve um excesso de: ", excesso, "kg")
  print("Sua multa será de R$", multa)
else:
  print("Peso aprovado!")
