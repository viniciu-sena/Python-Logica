#16
buy = 0.0
pay = 0.0
litro = 18
qtd = 0
m2 = 18 * 3

area = float( input("Valor da area em m2 que ira ser pintada: ") )

buy = area / m2

if "%.0f" % buy != buy: qtd = buy + 1
pay = qtd * 80
print("%.0f" % qtd ,  "latas serão necessarias para pintar a area custando o valor total de R$" , "%.2f" % pay)
