# Desenvolvido por Daniel Schinaider de Oliveira

# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# a. quantos espaços em branco existem na frase.
# b. quantas vezes aparecem as vogais a, e, i, o, u.

# Entrada de dado para string
frase = input("Informe uma frase: ")
# Instancia de variaveis inteiras
vogais = 0
espaco = 0
# Loop para percorrer as posicao da string
for i in range(len(frase)):
    # Condicao para detectar a presenca de vogais na variavel string
    if frase[i].lower() == "a" or frase[i].lower() == "e" or frase[i].lower() == "i" or frase[i].lower() == "o" or frase[i].lower() == "u":
    # Quando a condicao tornar verdadeira irá somar um a mais na variavel vogal
        vogais += 1
    # Condicao para detectar a presenca de espacos na variavel string
    if frase[i].isspace() == True:
    # Quando a condicao tornar verdadeira irá somar um a mais na variavel espaco
        espaco += 1
# Escreve a quantidade de vogais e espacos na variavel string
print(vogais, " vogais presentes na frase")
print(espaco, " espacos presentes na frase")