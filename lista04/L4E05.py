#05
numeros

numeros = []
par = []
impar = []

i = 0
while (i < 4):
  tec = int(input("Digite um numero: "))

  numeros.append(tec)

  if (tec % 2) == 0:
    par.append(tec)
  else:
    impar.append(tec)

  i+=1

print("Numeros:", numeros)
print("Par: ", par)
print("Impar:", impar)
