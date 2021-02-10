# Desenvolvido por Daniel Schinaider de Oliveira

# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

inp = int(input("Informe o valor de n: "))
def exer1(num):
    for i in range(num):
        i += 1
        print(str(i) * i)
exer1(inp)