# Desenvolvido por Daniel Schinaider de Oliveira
# Exercício número 12

horas = int( input("Informe a quantidade de horas trabalhadas no mês: "))
valorHora = float( input("Informe o seu valor hora: \n"))

bruto = horas * valorHora
inss = 0
ir = 0
fgts = 0
liquido = 0
desconto  = 0

if bruto <= 900:
  fgts = bruto * 0.11
  inss = bruto * 0.10
  liquid = bruto - inss
  print(" Salario bruto: R$",bruto)
  print("INSS: R$ %.2f" % inss)
  print("FGTS: R$ %.2f" % fgts)
  print("Total de descontos: R$ %.2f " % inss)
  print("Salario liquido: R$ %.2f" % liquid)

elif bruto > 900 and bruto <= 1500:
  fgts = bruto * 0.11
  inss = bruto * 0.10
  ir = bruto * 0.05
  desconto = ir + inss
  liquid = bruto - desconto
  print(" Salario bruto: R$",bruto)
  print("IR: R$ %.2f" % ir)
  print("INSS: R$ %.2f" % inss)
  print("FGTS: R$ %.2f" % fgts)
  print("Total de descontos: R$ %.2f " % desconto)
  print("Salario liquido: R$ %.2f" % liquid)

elif bruto > 1500 and bruto <= 2500:
  fgts = bruto * 0.11
  inss = bruto * 0.10
  ir = bruto * 0.10
  desconto = ir + inss
  liquid = bruto - desconto
  print(" Salario bruto: R$",bruto)
  print("IR: R$ %.2f" % ir)
  print("INSS: R$ %.2f" % inss)
  print("FGTS: R$ %.2f" % fgts)
  print("Total de descontos: R$ %.2f " % desconto)
  print("Salario liquido: R$ %.2f" % liquid)

elif bruto > 2500:
  fgts = bruto * 0.11
  inss = bruto * 0.10
  ir = bruto * 0.20
  desconto = ir + inss
  liquid = bruto - desconto
  print(" Salario bruto: R$",bruto)
  print("IR: R$ %.2f" % ir)
  print("INSS: R$ %.2f" % inss)
  print("FGTS: R$ %.2f" % fgts)
  print("Total de descontos: R$ %.2f " % desconto)
  print("Salario liquido: R$ %.2f" % liquid)
