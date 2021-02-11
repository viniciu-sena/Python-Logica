# Feito por Vinícius Silva Sena
#o4
class Pessoa:
  
  def _init_(self,nome,idade,peso,altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura
  
  def setNome(self,nome):
    self.nome = nome

  def setIdade(self,idade):
    self.idade = idade
  
  def setPeso(self,peso):
    self.peso = peso

  def setAltura(self,altura):
    self.altura = altura

  def getNome(self):
    return self.nome

  def getIdade(self):
    return self.idade

  def getPeso(self):
    return self.peso

  def getAltura(self):
    return self.altura

  def envelhecer(self,anos):
    if self.getIdade() <= 21:
      i = self.getIdade() + 1
      self.setIdade(self.getIdade() + anos)
      if self.getIdade() < 21:
        while i <= self.getIdade():
          self.setAltura(self.getAltura() + 0.05)
          i += 1
      else:
         while i <= 21:
          self.setAltura(self.getAltura() + 0.05)
          i += 1
    else:
      self.setIdade(self.getIdade() + anos)
    
  def engordar(self,quilo):
    self.setPeso(self.getPeso() + quilo)

  def emagrecer(self,quilo):
    self.setPeso(self.getPeso() - quilo)

  def crescer(self,cm):
    self.setAltura(self.getAltura() + cm)

  def getPessoa(self):
    altura = "{:.2f}".format(self.getAltura())
    print("nome: ",self.getNome()," | idade: ",self.getIdade(),
          " | altura: ",altura," | peso: ",self.getPeso())

vini = Pessoa()

vini.setNome("Vinicius")
vini.setIdade(13)
vini.setAltura(1.6)
vini.setPeso(40)

vini.getPessoa()
print("---------------------")
vini.envelhecer(4)
print("Envelhecer 3 anos: ")
vini.getPessoa()
print("---------------------")
vini.engordar(15)
print("Engordar 5 quilos")
vini.getPessoa()
print("---------------------")
vini.emagrecer(3)
print("Emagrecer 4 quilos")
vini.getPessoa()
print("---------------------")
vini.crescer(0.03)
print("Crescer 3cm")
vini.getPessoa()
