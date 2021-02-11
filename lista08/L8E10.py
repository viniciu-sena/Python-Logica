# Feito por Vinícius Silva Sena
#10
import math

class Posto:

  def _init_(self,tipo,valorLitro,litros):
    self.tipo = tipo
    self.valorLitro = valorLitro
    self.litros = litros
  
  def setTipo(self,tipo):
    self.tipo = tipo
  
  def setValorLitro(self,valorLitro):
    self.valorLitro = valorLitro

  def setLitros(self,litros):
    self.litros = litros

  def getTipo(self):
    return self.tipo

  def getValorLitro(self):
    return self.valorLitro

  def getLitros(self):
    return self.litros

  def abastecerValor(self):
    valor = float(input("Abastecer R$: "))
    litros = math.ceil(valor / self.getValorLitro())
    print("Voce abasteceu ",litros,"l de ",self.getTipo())
    self.setLitros(self.getLitros() - litros)

  def abastecerLitro(self):
    litros = float(input("Abastecer litros: "))
    valor = litros * self.getValorLitro()
    print("Total: R$",valor)
    self.setLitros(self.getLitros() - litros)
  
  def alterarValor(self):
    self.setValorLitro(float(input("Novo valor por litro: ")))

  def alterarTipo(self):
    self.setTipo(input("Novo tipo de combustivel: "))

  def alterarLitros(self):
    self.setLitros(float(input("Alterar litros armazenados: ")))
  
  def getPosto(self):
    print("Combustivel: ",self.getTipo()," | Litros R$: ",self.getValorLitro(),
          " | Litros restantes: ",self.getLitros())

def menu():
  print("----------------------------------------")
  print("1 - Abastecer por R$")
  print("2 - Abastecer por litros")
  print("3 - Alterar tipo de combustivel")
  print("4 - Abastecer litros armazenados")
  print("5 - Alterar valor por litro")
  print("0 - Sair")
  print("----------------------------------------")

sair = 0
choice = 0

posto = Posto()
posto.setTipo("Gasolina")
posto.setValorLitro(2.5)
posto.setLitros(400)

while sair == 0:
  posto.getPosto()
  menu()
  choice = int(input("Escolha: "))

  if choice == 1:
    posto.abastecerValor()
  elif choice == 2:
    posto.abastecerLitro()
  elif choice == 3:
    posto.alterarTipo()
  elif choice == 4:
    posto.alterarLitros()
  elif choice == 5:
    posto.alterarValor()
  else: 
    sair = 1

print("Fim :)")
