#11

salario = float(input("Digite seu salário: R$"))
porcent = 0

print("Salario base: R$",salario)
percent = 0
valor = salario

if (salario <= 280):
  percent = 20
  salario = salario * 1.2

elif (salario > 280 and salario <= 700):
  percent = 15
  salario = salario * 1.15

elif (salario > 700 and salario <= 1500):
  percent = 10
  salario = salario * 1.1

elif (salario > 1500):
  percent = 5
  salario = salario * 1.05

valor = salario - valor

print("Percentual de aumento: ",percent,"%")
print("Valor do aumento: R$ %.2f" % valor)
print("Salario com reaguste: R$ %.2f" % salario)
