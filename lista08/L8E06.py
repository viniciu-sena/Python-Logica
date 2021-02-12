# Feito por Daniel Schinaider de Oliveira
#06
class Tv:

  def _init_(self,canal,volume):
    self.canal = canal
    self.volume = volume
  
  def setCanal(self,canal):
    self.canal = canal
  
  def setVolume(self,volume):
    self.volume = volume

  def getCanal(self):
    return self.canal

  def getVolume(self):
    return self.volume

  def trocarCanal(self):
    canal = int(input("Informe o canal: "))
    if canal > 50:
      self.setCanal(50)
      print("Canal fora do escopo (redirecionado para o canal 50)")
    elif canal <= 0:
      self.setCanal(1)
      print("Canal fora do escopo (redirecionado para o canal 1)")
    else:
      self.setCanal(canal)

  def aumentarVolume(self):
    x = int(input("Quantas vezes: "))
    if (self.getVolume() + x) > 50:
      self.setVolume(50)
      print("Volume maximo é 50")
    else:
      self.setVolume(self.getVolume() + x)
  
  def diminuirVolume(self):
    x = int(input("Quantas vezes: "))
    if (self.getVolume() - x) < 0:
      self.setVolume(0)
      print("Mutado")
    else:
      self.setVolume(self.getVolume() - x)

  def getTv(self):
    print("Canal: ",self.getCanal()," | Volume: ",self.getVolume())

def menu():
  print("------------------------------")
  print("1 - Trocar de canal")
  print("2 - Aumentar o volume")
  print("3 - Diminuir o volume")
  print("0 - Desligar a TV")
  print("------------------------------")

tv = Tv()
tv.setCanal(1)
tv.setVolume(15)
ligado = True
choice = 0

while ligado == True:
  tv.getTv()
  menu()
  choice = int(input("Infome a opção desejada: "))
  if choice == 1:
    tv.trocarCanal()
  elif choice == 2:
    tv.aumentarVolume()
  elif choice == 3:
    tv.diminuirVolume()
  else:
    ligado = False

print("Televisor desligado")
