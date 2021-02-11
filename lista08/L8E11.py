# Feito por Kelvin Schneider
#11

class Carro:

  def __init__(self, consumo):
    self.consumo = consumo

  def adicionarGasolina(self, qtdCombustivel):
      self.qtdCombustivel = qtdCombustivel 

  def andar(self, distancia, qtdCombustivel, consumo):
    self.distancia = distancia
    self.qtdCombustivel = qtdCombustivel - (distancia / consumo)

  def obterGasolina(self, qtdCombustivel):
    self.qtdCombustivel = qtdCombustivel
    
    .
    print("Ainda restam %.2f" % self.qtdCombustivel, "Litros de gasolina no tanque")


meuFusca = Carro(15)                                            # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20)                                  # abastece com 20 litros de combustível. 
meuFusca.andar(100, meuFusca.qtdCombustivel, meuFusca.consumo)  # anda 100 quilômetros.
meuFusca.obterGasolina(meuFusca.qtdCombustivel)                 # Imprime o combustível que resta no tanque.
