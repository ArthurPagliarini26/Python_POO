class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def exibir_saldo(self):
        print(f"O saldo do titular {self.titular} é de {self.saldo}")

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, taxa_rendimento):
        super().__init__(titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    def render(self):
        self.saldo *= (1 + self.taxa_rendimento)
        print("Saldo atual: ", self.saldo)

    def exibir_saldo(self):
        super().exibir_saldo()

class ContaCorrente(Conta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def depositar(self, valor):
        if(valor < 1):
            print("Valor deve ser positivo")
        else:
            super().depositar(valor)

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")

contaPoupanca = ContaPoupanca("Arthur", 1000, 100)
contaCorrente = ContaCorrente("Igor", 1000, 10000)

contaPoupanca.depositar(300)
contaPoupanca.exibir_saldo()
contaPoupanca.render()

contaCorrente.depositar(300)
contaCorrente.exibir_saldo()

contaCorrente.sacar(300)
contaCorrente.exibir_saldo()


