#07
maior = 0

val01 = int(input("Informe o 1° valor: "))
val02 = int(input("Informe o 2° valor: "))
val03 = int(input("Informe o 3° valor: "))

valores = [val01,val02,val03]

for i in range(3):
  if valores[i] > maior:
    maior = valores[i]

menor = maior
for i in range(3):
  if valores[i] < menor:
    menor = valores[i]

print("O maior valor é: ", maior," e o menor é: ", menor)     
