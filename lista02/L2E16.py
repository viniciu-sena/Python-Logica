# Feito por Vinícius Silva Sena
#16
# Valores verificados para teste valido: A=1, B=2 e C=-15. 
# Os resultados devem ser raiz01=3 e raiz02=-5.
import math
import sys

a = 0
b = 0
c = 0
delta = 0
    
a = int(input("A: "))

if a == 0:
  sys.exit("'A' precisa ser diferente de 0 para dar sequencia a equação")
else:
  b = int(input("B: "))
  c = int(input("C: "))
  delta = pow(b,2)-(4*a*c)

if delta < 0:
  sys.exit("O Delta precisa ser positivo ou igual a 0")
elif delta == 0:
  print("Raiz (Delta=0): ",(-b/(2*a)))
else:
  raiz01 = (-b+math.sqrt(delta))/(2*a)
  raiz02 = (-b-math.sqrt(delta))/(2*a)
  print('Raizes: ',raiz01,' | ',raiz02)
