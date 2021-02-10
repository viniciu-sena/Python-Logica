# Feito por V1n1c1u5 51lv4 53n4
#14
palavra = input("Informe uma palavra: ").lower()

for char in palavra:
	if char == 'a':
		palavra = palavra.replace('a','4')
	elif char == 'i':
		palavra = palavra.replace('i','1')
	elif char == 'e':
		palavra = palavra.replace('e','3')
	elif char == 'l':
		palavra = palavra.replace('l','1')
	elif char == 'o':
		palavra = palavra.replace('o','0')
	elif char == 's':
		palavra = palavra.replace('s','5')
	elif char == 't':
		palavra = palavra.replace('t','7')
	else:
		pass

print(palavra)
