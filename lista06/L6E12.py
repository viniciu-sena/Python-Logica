# Feito por Kelvin Schneider
#12

numero = input("Digite um numero de telefone: ")
numero = numero.replace("-","")

if (len(numero) < 8):
    while len(numero) < 8:
        numero = "3" + numero

    numero = numero[:4] + "-" + numero[4:]
    print("Numero: ", numero)

elif (len(numero) > 8):
    print("Numero invalido")
