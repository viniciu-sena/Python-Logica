# Feito por Kelvin Schneider
#10

impar = [1, 3 ,5 , 7, 9 ,11 ,13, 15, 17, 19]
par = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print("Vetor com numeros impar: ", impar)
print("Vetor com numeros par: ", par)

def intercala(L,L2):
    numeros = []
    for a,b in zip(L, L2):
        numeros.append(a)
        numeros.append(b)
    return numeros

numeros = intercala(impar, par)

print("\n----------------------------------------------")
print("Numeros juntos: ", numeros)
