# Feito por Vinícius Silva Sena
#09
def reversor(n):
  nStr = str(n)
  aux = []
  i = len(nStr) - 1
  while i > -1:
    aux.append(list(nStr)[i])
    i -= 1
  for i in range(len(aux)):
    if i > 0:
      nStr = nStr + str(aux[i])
    else: 
      nStr = str(aux[i])
  return int(nStr)

n = int(input("Informe um valor: "))
print(reversor(n))
