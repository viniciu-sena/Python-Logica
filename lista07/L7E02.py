# Desenvolvido por Daniel Schinaider de Oliveira, Kelvin Schneider e Vinicius Sena

# Funcao responsável por ler o arquivo de texto no caminho especificado
def readFile():
    nome_arquivo = "C:\\Users\\Aluno\\usuario.txt"

    f = open(nome_arquivo, 'r')
    texto = f.readlines()
    return texto

# Funcao responsavel por criar arquivo de texto com enderecos ip validos e invalido dentro do caminho especificado
def createFile(texto):
    nome_arquivo = "C:\\Users\\Aluno\\relatorio.txt"
    f = open(nome_arquivo, 'w+')
    for i in range(len(texto)):
        f.write(str(texto[i]))
    f.close()
    return 0

def formateFile(numero, nome, porcent, soma, media):
    vetor = []
    vetor.append("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    vetor.append("------------------------------------------------------------------------\n")
    vetor.append("Nr.  Usuário        Espaço utilizado     % do uso\n")
    for i in range(len(numero)):
        vetor.append(str(int(i)+1)+"    ")
        vetor.append(nome[i]+"  ")
        vetor.append(str(numero[i])+"MB             ")
        vetor.append(str(porcent[i])+"%\n")

    vetor.append("\nEspaço total ocupado:"+ str(soma)+" MB")
    vetor.append("\nEspaço médio ocupado:"+ str(media)+" MB")

    return vetor

def filtro(texto):
    vetor = []
    nome = []
    numero = []
    porcent = []
    media = 0
    for x in range(len(texto)):
        nome.append(texto[x][0:15])

    for i in range(len(texto)):
        numero.append(float("{:.2f}".format(float(texto[i][16:])/1000000)))

    soma = 0
    for y in range(len(numero)):
        soma += numero[y]
    soma = float("{:.2f}".format(soma))

    for p in range(len(numero)):
        porcent.append(float("{:.2f}".format((100*numero[p]) / soma)))

    media = soma / len(numero)
    media = float("{:.2f}".format(media))

    vetor = formateFile(numero,nome,porcent,soma,media)

    createFile(vetor)


texto = readFile()
filtro(texto)