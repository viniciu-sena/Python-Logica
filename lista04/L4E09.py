# Feito por Vinícius Silva Sena
#09
a = []
for i in range(10):
  a.append(int(input("Informe o valor: ")))
soma = 0
for i in range(len(a)):
  soma += pow(a[i],2)
print("Soma dos quadrados: ",soma)
