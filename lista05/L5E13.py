# Feito por Kelvin Schneider
#13

linha = 15
coluna = 5

if (linha > 20): linha = 20
elif (linha < 1): linha = 1

if (coluna > 20): coluna = 20
elif (coluna < 1): coluna = 1

def pontas():
  print(("{}").format("+"), end="")

def funcLinha(linha):
  for i in range(linha):
    print(("{}").format("-"), end="")

def desenhar(coluna, linha):
  pontas()
  funcLinha(linha)
  pontas()
  
  for i in range(coluna):
    print(("\n{}").format("|" + " " * linha +"|"), end="")

  print("")
  pontas()
  funcLinha(linha)
  pontas()


desenhar(coluna, linha)
