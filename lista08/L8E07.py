# Feito por Vinícius Silva Sena
#07
class Tamagushi:

  def _init_(self,nome,fome,saude,idade):
    self.nome = nome
    self.fome = fome
    self.saude = saude
    self.idade = idade
  
  def setNome(self,nome):
    self.nome = nome

  def setFome(self,fome):
    self.fome = fome
  
  def setSaude(self,saude):
    self.saude = saude
  
  def setIdade(self,idade):
    self.idade = idade

  def getNome(self):
    return self.nome

  def getIdade(self):
    return self.idade
  
  def getFome(self):
    return self.fome
  
  def getSaude(self):
    return self.saude

  def alterarNome(self):
    nome = input("Novo nome: ")
    self.setNome(nome)
    print("Nome alterado!! - ",self.getNome())

  def alterarFome(self,choice):
    if choice == 1:
      if self.getFome() < 10:
        self.setFome(self.getFome() + 1)
        print(self.getNome()," foi alimentado :)")
      else:
        print(self.getNome()," não está com fome :)")
    else:
      self.setFome(self.getFome() - 1)
      print("CUIDADO! ",self.getNome()," não foi alimentado -_-")
  
  def alterarSaude(self,choice):
    if choice == 2:
      if self.getSaude() < 10:
        self.setSaude(self.getSaude() + 1)
        print(self.getNome()," foi tratado :)")
      else:
        print(self.getNome()," está saudavel :)")
    else:
      self.setSaude(self.getSaude() - 1)
      print("CUIDADO! ",self.getNome()," não foi tratado -_-")

  def alterarIdade(self):
    print(self.getNome()," está ficando mais velho")
    self.setIdade(self.getIdade() + 1)
  
  def getHumor(self):
    humor = (self.getFome() + self.getSaude()) / 2
    return humor

  def getTamagushi(self):
    print(self.getNome()," | Fome: ",self.getFome()," | Saude: ",self.getSaude(),
          " | Idade: ",self.getIdade()," | Humor: ",self.getHumor())

def menu(tamagushi):
  print("----------------------------------------")
  print("1 - Alimentar o ",tamagushi.getNome())
  print("2 - Tratar o ",tamagushi.getNome())
  print("3 - Trocar o nome do ",tamagushi.getNome())
  print("4 - Regras")
  print("0 - Game Over X-X ")
  print("----------------------------------------")

def regras():
  print("----------------------------------------")
  print(" Só é possivel escolher uma das opções por rodada,")
  print("as opções não escolhidas terão seu valor reduzido")
  print("no caso só fome e saude perderão 1 de valor.")
  print(" Caso o valor de saude seja menor que 2, fome seja menor que 4")
  print("ou humor seja menor que 3 o tamagushi morre.")
  print(" O humor é calculado com base na saude e fome ((fome + saude)/2).")
  print(" O Tamagushi envelhece a cada rodada (ele não morre por decorrencia idade)")
  print(" A opção regras não é considerada uma jogada")
  print("Jogue com sabedoria :)")
  print("----------------------------------------")

def evolution(pou,loop,choice):
  pou.alterarFome(choice)
  pou.alterarSaude(choice)
  pou.alterarIdade()

pou = Tamagushi()
pou.setNome("Pou")
pou.setIdade(1)
pou.setFome(8)
pou.setSaude(8)

gameOver = 0
loop = 1
choice = 0

while gameOver == 0:
  pou.getTamagushi()
  menu(pou)

  choice = int(input("Escolha: "))

  if choice == 4:
    regras()
  elif choice == 1 or choice == 2:
    evolution(pou,loop,choice)
  elif choice == 3:
    pou.alterarNome()
    evolution(pou,loop,choice)
  elif choice == 0:
    gameOver = 1
  else:
    gameOver = 1
  
  if pou.getFome() < 4:
    gameOver = 1
  elif pou.getHumor() < 3:
    gameOver = 1
  elif pou.getSaude() < 2:
    gameOver = 1
  else:
    pass

print("----------------------------------------")
print("GAME OVER :/")
