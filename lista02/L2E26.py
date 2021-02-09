# Feito por Kelvin Schneider
#26

print("Digite [A] - Alcool")
print("Digite [G] - Gasolina")
tipo = input("Digite o tipo de combustivel: ")
litros = float(input("Digite a quantidade de litros vendidos: "))

precoA = 1.90
precoG = 2.50

if (tipo.lower() == "a"):
  if (litros <= 20):
    desconto = (precoA * 1.03) - precoA 
    precoA = precoA - desconto
    preco = litros * precoA
  
  elif (litros > 20):
    desconto = (precoA * 1.05) - precoA 
    precoA = precoA - desconto
    preco = litros * precoA

elif (tipo.lower() == "g"):
  if (litros <= 20):
    desconto = (precoG * 1.04) - precoG 
    precoG = precoG - desconto
    preco = litros * precoG
  
  elif (litros > 20):
    desconto = (precoG * 1.06) - precoG 
    precoG = precoG - desconto
    preco = litros * precoG

print("O total a ser pago é: R$ %.2f" % preco)
