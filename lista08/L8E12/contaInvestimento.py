class ContaInvestimento:

    def _init_(self,saldo,taxa):
        self.saldo = saldo
        self.taxa = taxa

    def setSaldo(self,saldo):
        self.saldo = saldo

    def setTaxa(self,taxa):
        self.taxa = taxa

    def getSaldo(self):
        return self.saldo

    def getTaxa(self):
        return self.taxa

    def acioneJuros(self):
        self.setSaldo(self.getSaldo() + (self.getSaldo() * self.getTaxa()))