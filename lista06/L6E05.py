# Desenvolvido por Daniel Schinaider de Oliveira

# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

# Entrada de dado para variavel string
nome = str(input("Informe seu nome: "))
# Loop em forma decrescente que irá escrever a string em modo escada invertida
for x in range(len(nome), 0, -1):
    print(nome[:x])