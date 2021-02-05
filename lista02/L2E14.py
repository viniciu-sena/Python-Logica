nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

notas = [nota1, nota2]
10
media = (notas[0] + notas[1]) / len(notas)

if media >= 9 and media <= 10:
    print("sua nota é A")
elif media >= 7.5 and media < 9:
    print("sua nota é B")
elif media >= 6 and media < 7.5:
    print("sua nota é C")
elif media >= 4 and media < 6:
    print("sua nota é D")
else:
    print("sua nota é E")
