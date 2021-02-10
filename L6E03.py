# Desenvolvido por Daniel Schinaider de Oliveira

# 3 - Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
# Entrada de dado para variavel string
nome = str(input("Informe seu nome: "))

# loop para escrever o caracter de cada posicao da string
for x in range(len(nome)):
    print(nome[x])