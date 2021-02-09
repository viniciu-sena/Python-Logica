# Desenvolvido por Daniel Schinaider de Oliveira
# Exercício número 18

print("Formato da data dd/mm/aaaa")
date = input("Insira uma data: ")
dia = int(date.split("/")[0])
mes = int(date.split("/")[1])
ano = int(date.split("/")[2])
valid = 0
resto = 0
if ano > 0:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 0 and dia <= 31:
            print(dia, "/", mes, "/", ano)
            valid = 1
    if mes == 2:
        if (ano % 400) == 0:
            if dia > 0 and dia <= 29:
                valid = 1
    if (ano % 4) == 0 and (ano % 400) != 0 and (ano % 100) != 0:
        if dia > 0 and dia <= 29:
            valid = 1
    elif (ano % 4) != 0 or (ano % 100) == 0 or (ano % 400) != 0:
        if dia > 0 and dia <= 28:
            valid = 1

    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 0 and dia <= 30:
            valid = 1

if valid == 1:
    print("Esta data é valida")
else:
    print("Data Invalida")
