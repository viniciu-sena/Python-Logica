print("Morango e Maca")
qtdMaca = float(input("Informe a quantidade(kgs) de maçãs que deseja comprar: "))

if qtdMaca <= 5:
    totalMaca = float(qtdMaca * 1.80)
elif qtdMaca > 5:
    totalMaca = float(qtdMaca * 1.50)

qtdMorango = float(input("Informe a quantidade(kgs) de morangos que deseja comprar: "))

if qtdMorango <= 5:
    totalMorango = float(qtdMaca * 2.50)
elif qtdMorango > 5:
    totalMorango = float(qtdMaca * 2.20)
total = totalMorango + totalMaca
if qtdMaca >= 8 or qtdMorango >= 8 or totalMorango > 25 or totalMaca > 25:
    desconto = float(total * 0.10)
    total = total - desconto
    print("Você conseguiu um desconto de R$ %.2f " % desconto)
print("Você adquiriu %.2f" % qtdMaca , "kgs de Maçãs")
print("Você adquiriu %.2f" % qtdMorango , "kgs de Morangos")
print("Você irá pagar R$ %.2f" % total)