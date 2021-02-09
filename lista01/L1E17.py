# Feito por Vinícius Silva Sena
#17

import math

area = float(input("Digite o tamanho da area a ser pintada (m²): "))

litros = (area / 6) * 1.1

tudoGalao = math.ceil((float(litros)/3.6))
tudoLata = math.ceil((float(litros)/18))


print("Quantidade apenas em Galao: ", tudoGalao, " | R$", tudoGalao * 25.0) 
print("Quantidade apenas em Lata: ", tudoLata, " | R$", tudoLata * 80.0) 

qtdLata = float(float(litros//18))
qtdGalao = math.ceil((float(litros) - float(qtdLata * 18)) / 3.6)

valorT = (qtdLata * 80) + (qtdGalao * 25)

print("-------------- MISTO -----------------")
print("Quantidade de latas: ", qtdLata)
print("Quantidade de galao: ", qtdGalao)
print("Valor: R$", valorT)
