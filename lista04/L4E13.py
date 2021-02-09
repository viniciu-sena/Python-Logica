# Desenvolvido por Daniel Schinaider de Oliveira
# Exercício número 13

temp = [] * 12
months = ["janeiro",  "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
somaMedias = 0
mediaYearly = 0

for i in range(0, 12):
    print(months[i])
    temp.append(float(input("Informe a temperatura:")))

for y in range(0, len(temp)):
    somaMedias += temp[y]
mediaYearly = somaMedias / len(temp)
print("\n Meses com a temperatura média maior que a anual",mediaYearly , " °C")
for a in range(0, len(temp)):
    if temp[a] > mediaYearly:
        if a == 1:
            print("1 - Janeiro: ", temp[a], "°C")
        if a == 2:
            print("2 - Fevereiro: ", temp[a], "°C")
        if a == 3:
            print("3 - Março : ", temp[a], "°C")
        if a == 4:
            print("4 - Abril : ", temp[a], "°C")
        if a == 5:
            print("5 - Maio : ", temp[a], "°C")
        if a == 6:
            print("6 - Junho : ", temp[a], "°C")
        if a == 7:
            print("7 - Julho: ", temp[a], "°C")
        if a == 8:
            print("8 - Agosto: ", temp[a], "°C")
        if a == 9:
            print("9 - Setembro: ", temp[a], "°C")
        if a == 10:
            print("10 - Outubro: ", temp[a], "°C")
        if a == 11:
            print("11 - Novembro: ", temp[a], "°C")
        if a == 12:
            print("12 - Dezembro: ", temp[a], "°C")

#