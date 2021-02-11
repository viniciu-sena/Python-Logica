# Feito por Kelvin Schneider
#10

numero = int(input("Digite um numero de 1 a 99: "))

num1 = ["","vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
num2 = ["um", "dois", "tres", "quatro" , "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

if (numero >= 1 and numero <= 99):
  if (numero > 19): 
    numero = str(numero)

    for i in range(1, 10):
      if (int(numero[0]) == i):
        parte1 = num1[i-1]

    for i in range(1, 10):
      if (int(numero[1]) == i):
        parte2 = num2[i-1]
    
    numeroEx = parte1 + " e " + parte2

  else:
    for i in range(1, 20):
      if (int(numero) == i):
        numeroEx = num2[i-1]

  print("Numero: ", numeroEx)
else:
  print("Numero invalido")
