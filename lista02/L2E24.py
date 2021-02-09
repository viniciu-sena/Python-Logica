# Feito por Vinicius Silva Sena
#24

num1 = float( input("Digite o valor 1: "))
num2 = float( input("Digite o valor 2: "))
result = 0
print("1 para multiplicacao")
print("2 para divisao")
print("3 para adicao")
print("4 para subtracao")
inp = int(input(">>"))

if inp == 1:
  result = num1 * num2
  if result % 2 == 0:
    print("Par")
  else: print("Impar")
  if result > 0:
    print("Positivo")
  else:print("Negativo")
  if int(result) == result:
    print("Inteiro")
  else: print("Decimal")
  print(num1 , " * " , num2 , " = " , result)

elif inp == 2:
    result = num1 / num2
    if result % 2 == 0:
        print("Par")
    else:
        print("Impar")
    if result > 0:
        print("Positivo")
    else:
        print("Negativo")
    if int(result) == result:
        print("Inteiro")
    else:
        print("Decimal")
    print(num1, " / ", num2, " = ", result)

elif inp == 3:
    result = num1 + num2
    if result % 2 == 0:
        print("Par")
    else:
        print("Impar")
    if result > 0:
        print("Positivo")
    else:
        print("Negativo")
    if int(result) == result:
        print("Inteiro")
    else:
        print("Decimal")
    print(num1, " + ", num2, " = ", result)

elif inp == 4:
    result = num1 - num2
    if result % 2 == 0:
        print("Par")
    else:
        print("Impar")
    if result > 0:
        print("Positivo")
    else:
        print("Negativo")
    if int(result) == result:
        print("Inteiro")
    else:
        print("Decimal")
    print(num1, " - ", num2, " = ", result)
