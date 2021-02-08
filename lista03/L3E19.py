#19
n = int(input("N° de valores: "))

i = 0
valores = []

while i < n:
    valor = int(input("informe o valor: "))
    if not (valor < 0 or valor > 1000):
      valores.append(valor)
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
