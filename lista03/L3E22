# Feito por Vinícius Silva Sena
#22
import sympy

valor = int(input("Informe o valor: "))
divisores = []

if sympy.isprime(valor) == False:
  for i in range(valor):
     if (valor % (i+1)) == 0:
       divisores.append(i+1)
  print("Não é primo, é divisivel por: ",divisores)
else:
  print("Primo")
