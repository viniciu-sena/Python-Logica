# Feito por Kelvin Schneider
#15

lado1 = float(input("Digite o tamanho do lado1 do triangulo:"))
lado2 = float(input("Digite o tamanho do lado2 do triangulo:"))
lado3 = float(input("Digite o tamanho do lado3 do triangulo:"))



if (lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1):
  if (lado1 == lado2 and lado2 == lado3):
    forma = "Equilatero"
  
  elif (lado1 != lado2 and lado2 != lado3):
    forma = "Escaleno"
  
  elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    forma = "Isóceles"

  print("Essas medidas formam um triangulo ", forma)

else:
  print("Essas medidas não formam um triangulo!")
