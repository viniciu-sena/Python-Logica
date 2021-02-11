# Feito por Kelvin Schneider
#08

print("------------- Palindromo -----------------")
texto = input("Digite uma palavra/frase: ")

texto = texto.lower()
texto = texto.replace(" ","")

if (texto == texto[::-1]):
  print("Isso é um polindromo")
else:
  print("Não é um polindromo")
