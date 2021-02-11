# Feito por Kelvin Schneider
#06

print("--------------DATA DE NASCIMENTO----------------")
dia = int(input("Digite o dia [DD]: "))
mes = int(input("Digite o mes [MM]: "))
ano = int(input("Digite o ano [AAAA]: "))
print("Data de Nascimento: ", dia,"/",mes,"/",ano)

def data(dia,mes,ano):
  if (mes == 1): mes = "Janeiro"
  elif (mes == 2): mes = "Fevereiro"
  elif (mes == 3): mes = "Março"
  elif (mes == 4): mes = "Abril"
  elif (mes == 5): mes = "Maio"
  elif (mes == 6): mes = "Junho"
  elif (mes == 7): mes = "Julho"
  elif (mes == 8): mes = "Agosto"
  elif (mes == 9): mes = "Setembro"
  elif (mes == 10): mes = "Outubro"
  elif (mes == 11): mes = "Novembro"
  elif (mes == 12): mes = "Dezembro"
  elif (mes > 12 or dia > 31 or mes < 1 or dia < 1 or ano < 1): print("NULL")

  print("\nVocê nasceu em: \n", dia,"de", mes,"de", ano)

data(dia,mes,ano)
