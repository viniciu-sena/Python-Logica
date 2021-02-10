# Desenvolvido por Daniel Schinaider de Oliveira

# 1 - Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Entrada de dados nas variaveis do tipo string
string1 = input("Informe 1 string: ")
string2 = input("Informe 2 string: ")

# Print do dado encontrado nas variaveis string
print("String 1: ", string1)
print("String 2: ", string2)

# Print da quantidade de caracteres inseridos nas variaveis
print("Tamanho de '",string1,"':", len((string1)), "caracteres")
print("Tamanho de '",string2,"':", len((string2)), "caracteres")

# condicao para identificar se as variaveis apresentam a mesma quantidade de caracteres
if len(string1) == len(string2):
    print("As duas strings são de tamanhos iguais")
else:
    print("As duas strings são de tamanhos diferentes.")

# Condicao para analisar se as variaveis tem dado identico
if string1 == string2:
    print("As duas strings possuem conteúdos iguais")
else:
    print("As duas strings possuem conteúdo diferente.")