# Feito por Vinícius Silva Sena
#06
a = ' A.M'
p = ' P.M'
x = 0
y = 0
sair = 0

def converteHora(x,y):
  if x > 12:
    x = x - 12
    return printHora(p,x,y)
  else:
    return printHora(a,x,y)

def printHora(n,x,y):
  if n == p:
    return str(str(x) + ":" + str(y) + p)
  else:
    return str(str(x) + ":" + str(y) + a)

while sair == 0:
  x = int(input("Infome as horas: "))
  y = int(input("Infome os minutos: "))
  if x > 24 or x < 0 or y < 0 or y > 60:
    print("Horas ou minutos invalidos")
  else:
    print(converteHora(x,y))
  sair = int(input("Tecle 0 para continuar: "))
