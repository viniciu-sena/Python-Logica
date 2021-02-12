# Feito por Daniel Schinaider de Oliveira
#12
from contaInvestimento import ContaInvestimento
from contaBancaria import ContaBancaria

investimento = ContaInvestimento()
poupanca = ContaBancaria()

poupanca.setSaldo(1000)
investimento.setSaldo(poupanca.getSaldo())
investimento.setTaxa(0.1)

investimento.acioneJuros()
investimento.acioneJuros()
investimento.acioneJuros()
investimento.acioneJuros()
investimento.acioneJuros()

print("Juros aplicados 5x R$",investimento.getSaldo())