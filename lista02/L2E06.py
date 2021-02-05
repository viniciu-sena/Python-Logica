maior = 0
num1 = float(input("Digite o 1° valor: "))
num2 = float(input("Digite o 2° valor: "))
num3 = float(input("Digite o 3° valor: "))
numbers = [num1, num2, num3]

for i in range(3):
    if numbers[i] > maior:
        maior = numbers[i]


else:
    print("O maior número digitado foi: ", maior)
