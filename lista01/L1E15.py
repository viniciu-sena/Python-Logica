#15
valor = float(input("Valor hora: "))
hora = int(input("Horas trablhadas por mes: "))

salario = (valor*hora)

print("Salario bruto: ", salario)
print("INSS: ", (salario*0.08))
print("Sindicato: ", (salario*0.05))
print("Imposto de renda: ", (salario*0.11))
print("Salario liquido: ", (salario - (salario*0.24)))
