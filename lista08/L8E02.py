# Feito por Kelvin Schneider
#02

'''Como no exercicio não estava especificado, deixei um valor pré definido
e dentro do método é aumentado o tamanho do lado em 10%'''

class Quadrado:
  def __init__(self, tLado):
    self.tLado = tLado

  def mudarValor(self, tLado):
    self.tLado = tLado * 1.1
    print("Area :", self.tLado)

  tLado = 20

classQuadrado = Quadrado(tLado)
classQuadrado.mudarValor(tLado)
