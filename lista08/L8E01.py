# Feito por Vinícius Silva Sena
#01

class Bola:

  def _init_(self,cor,cfc,material):
    self.cor = cor
    self.cfc = cfc
    self.material = material
  
  def setCor(self,cor):
    self.cor = cor

  def setCfc(self,cfc):
    self.cfc = cfc
  
  def setMaterial(self,material):
    self.material = material
  
  def getCor(self):
    return self.cor

  def getCfc(self):
    return self.cfc
  
  def getMaterial(self):
    return self.material
  
  def getBola(self):
    print(self.getCor()," - ",self.getCfc()," - ",self.getMaterial())

bola = Bola()

bola.setCor(input("Informe a cor:  "))
print("Old cor: ",bola.getCor())
bola.setCfc(float(input("Informe a circunferencia:  ")))
bola.setMaterial(input("Informe o material:  "))
bola.setCor("Cor trocada XD")
print("New cor: ",bola.getCor())

bola.getBola()
