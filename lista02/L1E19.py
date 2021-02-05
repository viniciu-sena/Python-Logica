#19
import sys
numero = int(input("Insira um numero menor que 1000 e maior que 0: "))

if numero <= 0 or numero > 1000:
  sys.exit("O numero informado precisa ser maior que 0 e menor que 1000")

unidade = numero % 10
dezena = ((numero % 100)-unidade)/10
centena = ((numero % 1000)-(dezena*10)-unidade)/100

print(centena," centenas, ",dezena," dezenas e ",unidade," unidades")
