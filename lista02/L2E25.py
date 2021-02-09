# Feito por Vinícius Silva Sena
#25
relatorio = []

print("Responda com s/n")
relatorio.append(input("Telefonou para a vitima? "))
relatorio.append(input("Esteve no local do crime? "))
relatorio.append(input("Mora perto da vítima? "))
relatorio.append(input("Devia para a vítima? "))
relatorio.append(input("Já trabalhou com a vítima? ")) 

val = relatorio.count("s")

if val == 2:
  print("Suspeito")
elif val > 2 and val <= 4:
  print("Cumplice")
elif val == 5:
  print("Assassino")
else:
  print("Inocente")
