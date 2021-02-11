# Feito por Kelvin Schneider
#05

class ContaCorrente:
  def __init__(self, nConta, nome, saldo):
    self.nConta = nConta
    self.nome = nome
    self.saldo = saldo

  def alterarConta(self, nConta):
    novoNum = int(input("\nDigite seu numero: "))
    self.nConta = novoNum
    print("Numero da conta alterado com sucesso!")

  def alterarNome(self, nome):
    novoNome = str(input("\nDigite seu nome: "))
    self.nome = novoNome
    print("Nome alterado com sucesso!")

  def alterarSaldo(self, saldo):
    novoSaldo = int(input("\nDigite seu saldo: "))
    self.saldo = novoSaldo
    print("Saldo alterado com sucesso!")

  nConta, nome, saldo = 888999, "Kelvin Schn", 2000

contaCorrente = ContaCorrente(nConta, nome, saldo)

print("\n---- DADOS PRÉ DEFINIDOS -----")
print("Numero da Conta: ", nConta)
print("Nome: ", nome)
print("Saldo: ", saldo)

res = "s"

while res == "s": 
  print("\nDigite o numero do que deseja alterar: ")
  print("[1] - Número da Conta")
  print("[2] - Nome")
  print("[3] - Saldo")
  n = int(input("> "))

  if (n > 3 or n < 1):
    print("\nopção invalida")
  else:
    if (n == 1): contaCorrente.alterarConta(nConta)
    elif (n == 2): contaCorrente.alterarNome(nome)
    elif (n == 3): contaCorrente.alterarSaldo(saldo)
  
  res = str(input("\nDeseja fazer mais uma alteração [s/n]: "))

print("\n---- NOVOS DADOS -----")
print("Numero da Conta: ", contaCorrente.nConta)
print("Nome: ", contaCorrente.nome)
print("Saldo: ", contaCorrente.saldo)
print("Programa Finalizado")
