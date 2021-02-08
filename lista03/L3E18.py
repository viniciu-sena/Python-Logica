# Feito por Vinícius Silva Sena
#18
n = int(input("N° de valores: "))

i = 0
valores = []

while i < n:
    valores.append(int(input("informe o valor: ")))
    i += 1

maior = 0
soma = 0

for i in range(len(valores)):
  soma += valores[i]
  if valores[i] >= maior:
    maior = valores[i]

menor = maior

for i in range(len(valores)):
  if valores[i] <= menor:
    menor = valores[i]

print("Maior: ",maior," | Menor: ",menor," | Soma: ",soma)
