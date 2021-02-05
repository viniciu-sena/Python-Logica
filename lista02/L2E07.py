#07
maior = 0
valores = []

i = 0
while i < 3:
  valores.append(int(input("Informe o valor: ")))
  i += 1

for i in range(3):
  if valores[i] > maior:
    maior = valores[i]

menor = maior
for i in range(3):
  if valores[i] < menor:
    menor = valores[i]

print("O maior valor é: ", maior," e o menor é: ", menor)         
