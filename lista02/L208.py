#08

prod = []

i=0
while (i < 3):
  prod.append(float(input("Digite o preço do produto: ")))
  i+=1

maior = 0 

x=0
while (x < 3):
  if (prod[x] > maior):
    maior = prod[x]
  x+=1

menor = maior

y=0
while (y < 3):
  if (prod[y] < menor):
    menor = prod[y]
  y+=1

print("O menor preço é : %.2f" % menor)
