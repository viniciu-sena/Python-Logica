# Desenvolvido por Daniel Schinaider de Oliveira
#03
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
salario = float(input("Informe seu salário: "))
sexo = input("Informe seu sexo: ")
estado_civil = input("Informe a inicial do seu estado civil: ")
print("\n")
print("\n")

while len(nome) < 4:
  print("\n Nome inválido")
  nome = input("Informe seu nome novamente: ")

print("\n")

while int(idade) < 1 or int(idade) > 149:
  print("\n Idade inválida")
  idade = int(input("Informe sua idade novamente: "))

print("\n")

while float(salario) <= 0:
  print("\n Salário inválido")
  salario = float(input("Informe seu salário novamente: "))

print("\n")

while sexo.lower() != "f" and sexo.lower() != "m":
  print("\n Sexo inválido")
  sexo = input("Informe seu sexo novamente: ")

print("\n")

while estado_civil.lower() != "s" and estado_civil.lower() != "c" and estado_civil.lower() != "v" and estado_civil.lower() != "d":
  print("\n Estado civil inválido")
  estado_civil = input("Informe a inicial do seu estado civil novamente: ")

print("\n")

print("Seus dados informados: ")
print("Nome: " , nome)
print("idade: " , idade)
print("Salario: R$ %.2f" % salario)
print("Sexo: ", sexo)
print("Estado Civil: ", estado_civil)


