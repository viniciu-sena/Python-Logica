# Desenvolvido por Daniel Schinaider de Oliveira
# Exercício número 28
print("  Tipos          Até 5 kg        Acima de 5 kg\n"
      " 1) FileDuplo    R$4.90 por KG   R$5.80 por KG\n"
      " 2) Alcatra      R$5.90 por KG   R$6.80 por KG\n"
      " 3) Picanha      R$6.90 por KG   R$7.80 por KG\n")

tipo = input("Escolha o tipo de carne: ")
qtd = float(input("Escolha a quantidade(KG): "))
total = 0
desconto  = 0

print("1 - Cartão tabajara\n"
      "2 - Dinheiro\n"
      "3 - Débito/Crédito\n")
escolha = input("Informe o número da sua escolha de pagamento: \n")

if tipo == "1":

    print("Tipo de Carne: Filé Duplo")
    if qtd <= 5:
        total = qtd * 4.90
    elif qtd > 5:
        total = qtd * 5.80
    print("Quantidade de carne: %.2f" % qtd , "Kgs")
    print("Preço Total: R$ %.2f" % total)

elif tipo == "2":

    print("Tipo de Carne: Alcatra")
    if qtd <= 5:
        total = qtd * 5.90
    elif qtd > 5:
        total = qtd * 6.80
    print("Quantidade de carne: %.2f" % qtd , "Kgs")
    print("Preço Total: R$ %.2f" % total)

elif tipo == "3":

    print("Tipo de Carne: Picanha")
    if qtd <= 5:
        total = qtd * 6.90
    elif qtd > 5:
        total = qtd * 7.80
    print("Quantidade de carne: %.2f" % qtd , "Kgs")
    print("Preço Total: R$ %.2f" % total)

if escolha == "1":
    print("Tipo de Pagamento: Cartão Tabajara")
    desconto = total * 0.05
    total = total - desconto
elif escolha == "2":
    print("Tipo de Pagamento: Dinheiro")
elif escolha == "3":
    print("Tipo de Pagamento: Débito/Crédito")

print("Valor de Desconto: R$ %.2f" % desconto)
print("Total a pagar: R$ %.2f" % total)




