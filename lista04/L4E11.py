# Feito por Kelvin Schneider
#11

lista1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
lista2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
lista3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

print("Vetor com numeros impar: ", impar)
print("Vetor com numeros par: ", par)

def intercala(L,L2, L3):
    numeros = []
    for a,b,c in zip(L, L2, L3):
        numeros.append(a)
        numeros.append(b)
        numeros.append(c)
    return numeros

numeros = intercala(lista1, lista2, lista3)

print("\n----------------------------------------------")
print("Numeros juntos: ", numeros)
