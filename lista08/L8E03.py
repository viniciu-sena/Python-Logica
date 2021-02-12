# Feito por Daniel Schinaider de Oliveira
#03

class Retangulo:
    def __init__(self, ladoA, ladoB, pisoA, pisoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.pisoA = pisoA
        self.pisoB = pisoB

    def mudarValor(self, ladoA, ladoB):
        self.ladoA = float(input("Digite a largura do local em metros: "))
        self.ladoB = float(input("Digite o comprimento do local em metros: "))

    def retornarValor(self, ladoA, ladoB):
        print("\nLargura do local: ", ladoA,"m")
        print("Comprimento do local: ", ladoB,"m")

    def calcularArea(self, ladoA, ladoB, pisoA, pisoB):
        self.area = ladoA * ladoB
        self.areaP = pisoA * pisoB

    def calcularPerimetro(self, ladoA, ladoB):
        self.perim = (ladoA + ladoB) * 2

    def calcularPiso(self, area, areaP, perim, pisoB):
        self.qtdPiso = area / areaP
        self.qtdRodape = perim / pisoB

        print("\nQuantidade de pisos necessários: ",round(self.qtdPiso))
        print("Quantidade de rodapé necessários: ",round(self.qtdRodape))

ladoA = float(input("Digite a largura do local em metros: "))
ladoB = float(input("Digite o comprimento do local em metros: "))
pisoA = float(input("Digite a largura do piso em metros: "))
pisoB = float(input("Digite o comprimento do piso em metros: "))

local = Retangulo(ladoA, ladoB, pisoA, pisoB)
local.retornarValor(ladoA,ladoB)

res = str(input("\nDeseja mudar os valores do local? [s/n]: "))
if (res == "s"):
    local.mudarValor(local.ladoA, local.ladoB)

local.calcularArea(local.ladoA, local.ladoB, local.pisoA,local.pisoB)
local.calcularPerimetro(local.ladoA, local.ladoB)
local.calcularPiso(local.area, local.areaP, local.perim, pisoB)