num1 = -1
while num1 < 0 or num1 > 10:
   num1 = float(input("Informe uma nota entre 0 e 10: "))
   if num1 > 10 or num1 < 0:
        print("Nota com valor inválido!")
   else:
        print("Nota com valor de " , num1 , " é válida!")