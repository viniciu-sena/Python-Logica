# Feito por Kelvin Schneider
#04

class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimirValores(self):
        print("Ponto: (", self.x, ",", self.y, ")")

class Rentangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self, x, y):
        self.centroX = x + (largura / 2)
        self.centroY = y + (altura / 2)


largura = float(input("Digite a largura do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))

x = float(input("Digite o ponto X para a vertice inicial: "))
y = float(input("Digite o ponto Y para a vertice inicial: "))

vertice = Ponto(x, y)

r1 = Rentangulo(largura, altura)
r1.encontrarCentro(vertice.x, vertice.y)

pontoCentro = Ponto(r1.centroX, r1.centroY)

print("\nPonto central: ")
pontoCentro.imprimirValores()
