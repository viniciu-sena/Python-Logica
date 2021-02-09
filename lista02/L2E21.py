# Feito por Vinícius Silva Sena
#21
valor = int(input("Informe o valor do saque: "))

nota100 = int(valor/100)
valor = valor-(nota100*100)

nota50 = int(valor/50)
valor = valor-(nota50*50)

nota10 = int(valor/10)
valor = valor-(nota10*10)

nota5 = int(valor/5)
valor = valor-(nota5*5)

print("R$1: ",valor, " | R$5: ",nota5," | R$10: ",nota10,
      " | R$50: ",nota50," | R$100: ",nota100)

