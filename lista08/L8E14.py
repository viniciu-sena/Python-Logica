# Feito por Kelvin Schneider
#14

class Funcionario:
  
  def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario

  def mostrarFunci(self, nome, salario):
    print("Funcionario: ", self.nome)
    print("Salário: ", self.salario)

  def aumentarSalario(self, porcent,salario):
    self.salario = salario + (salario * (porcent / 100))

kelvin = Funcionario("Kelvin", 2000)
kelvin.aumentarSalario(10, kelvin.salario) #Aumento de 10 porcento do salario
kelvin.mostrarFunci(kelvin.nome, kelvin.salario)

print("-----------------------------")

pedro = Funcionario("Pedro", 4000)
pedro.aumentarSalario(20, pedro.salario)
pedro.mostrarFunci(pedro.nome, pedro.salario)
