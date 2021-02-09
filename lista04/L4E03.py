# Feito por Vinícius Silva Sena
#03
notas = []
soma = 0
for i in range(4):
  notas.append(float(input("Informe a nota: ")))
  soma += notas[i]
for i in range(len(notas)):
  print("Nota: ",notas[i])
print("Media: ",(soma/4))
