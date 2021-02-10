# Desenvolvido por Daniel Schinaider de Oliveira

#   Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se
#   é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

print("Validador de CPF")
print("Formato usado: xxx.xxx.xxx-xx")

# Entrada de dados para variavel string
cpf = str(input("Informe seu cpf: "))

# Instancia de variaveis inteiras
aux1 = 0
aux2 = 0
soma1 = 0
soma2 = 0
digit10 = 0
digit11 = 0

# Funcao responsavel por validar o formato do cpf
def validar(cpf):
    print(len(cpf))
    # Condicao que ira analisar se algumas posicoes da variavel string possuem determinado caracter
    if cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
        return True
    else:
        return False

# Funcao responsavel por adicionar somente os numeros do cpf em um vetor
def convertVetor(cpf):
    vetor= []
    aux = 0
    for i in range(len(cpf)):
    # Condicao que só ira retornar true caso o caracter da posicao for um numero
        if cpf[i].isnumeric():
            # Vetor adiciona o numero determinado por i na variavel string cpf
            vetor.append(cpf[i])
    aux = vetor
    # retorna o vetor com os numeros do cpf
    return aux

# Funcao responsavel por multiplicar o caracter da posicao 0 ate a 8 por numeros na ordem decrescente de 10 até 2
def firstValidation(cpf):
    soma = 0
    x = 10
    for i in range(len(cpf)):
        # Condicao responsavel por verifica que enquanto o i for menor que 9 essa conta continuara a ser executada
        if i < 9:
            # Variavel se soma constantemente ao resultado da multiplicacao
            soma += int(cpf[i]) * x
        # Condicao quebra o loop
        else:
            break
        x -= 1
    # retorna a soma total do resultado das multplicacoes
    return soma

# Funcao responsavel por multiplicar o caracter da posicao 0 ate a 8 por numeros na ordem decrescente de 11 até 2
def secondvalidation(cpf):
    soma = 0
    x = 11
    for i in range(len(cpf)):
        # Condicao responsavel por verifica que enquanto o i for menor que 10 essa conta continuara a ser executada
        if i < 10:
            # Variavel se soma constantemente ao resultado da multiplicacao
            soma += int(cpf[i]) * x
        # Condicao quebra o loop
        else:
            break
        x -= 1
    # retorna a soma total do resultado das multplicacoes
    return soma

# Funcao responsavel por validar o cpf
def validationCpf(soma1, soma2, vetor):
    # variavel que ira receber o resultado do valor total da soma dos resultados das multiplicacoes e multiplicar por 10
    digit10 = (soma1 * 10)
    digit11 = (soma2 * 10)

    # Variavel que ira receber o resto da divisao de digit10 e digit11 e 11
    resto1 = digit10 % 11
    resto2 = digit11 % 11

    # Condicao que ira verificar se as variaveis de resto são identicas as duas ultimas posicoes do vetor de com numeros do cpf
    if resto1 == int(vetor[9]) and resto2 == int(vetor[10]):
        # Retorna que ele é valido
        return True
    else:
        # Retorna que ele é invalido
        return False

# Funcao para chamar as validacoes do cpf
def chamada():
    if validar(cpf) == True:
        print("Formato válido!")
        # Variaveis responsaveis por armazenar o retorno das funcoes e chamar as mesmas
        auxCpf = convertVetor(cpf)
        soma1 = firstValidation(auxCpf)
        soma2 = secondvalidation(auxCpf)
        if validationCpf(soma1, soma2, auxCpf) == True:
            print("O Cpf é válido!")
        else:
            print("Este cpf é invalido")
    else:
        print("Use o formato especificado!")
        print("Formato inválido!")

# Chamar a funcao chamada
chamada()