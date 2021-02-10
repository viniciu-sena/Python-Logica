# Desenvolvido por Daniel Schinaider de Oliveira

# 7 - Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valor, dias):
     pagamento = 0.0
     if dias < 1:
         pagamento = valor
         print("Valor a ser pago R$%.2f" % valor)
         return pagamento
     else:
         pagamento = float((valor * 0.3 ) + ((dias * 0.01) * valor) + valor)
         return pagamento

qtd = 0
valorTot = 0
valores = []
while True:
    qtd += 1
    prestacoes = float(input("Informe o valor das prestacoes: "))

    if prestacoes == 0:
        break

    atraso = int(input("Informe a quantidade de dias atrasados: "))

    valores.append(valorPagamento(prestacoes, atraso))

for i in range(len(valores)):
    valorTot = valorTot + valores[i]

print("Relatório do Dia")
print("Quantidade de prestacoes pagas: " , qtd)
for i in range(len(valores)):
    print("Valor da prestacao R$", valores[i])

print("Valor total de prestacoes R$", valorTot)