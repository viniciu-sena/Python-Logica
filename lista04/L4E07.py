# Desenvolvido por Daniel Schinaider de Oliveira
# Exercício número 7

array = [1,2,4,5,6]

for i in range(0 , len(array)):
    for a in range(0, len(array)):
        mult = array[i] * array[a]
        print(array[i] , "x" , array[a] , "=" ,mult)
    print("\n")
for i in range(0 , len(array)):
    for a in range(0, len(array)):
        soma = array[i] + array[a]
        print(array[i] , "+" , array[a] , "=" ,soma)
    print("\n")
for i in range(0, len(array)):
    print(array[i])