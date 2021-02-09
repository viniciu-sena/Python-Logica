# Feito por Vinícius Silva Sena
#13
sex = input("Digite M para identificar seu sexo como masculino ou F para feminino:")
h = float( input("Digite sua altura: ") )

if sex.lower() == "m":
  h = (72.7*h) - 58
  print("%.2f" % h, "kg é seu peso ideal" )
elif sex.lower() == "f":
  h = (62.1*h) - 44.7
  print("%.2f" % h, "kg é seu peso ideal" )
