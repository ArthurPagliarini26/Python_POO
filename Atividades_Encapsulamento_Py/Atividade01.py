class Cofre:
    def __init__(self, valor, nome):
        self.nome = nome
        self.__valor = valor

    def get_valor(self):
        return self.__valor


    def depositar(self, valor):
        if(valor <= 0):
            print("Valor invalido")
        else:
            self.__valor += valor

    def retirar(self, valor):
        if(valor > self.__valor):
            print("Valor invalido")
        else:
            self.__valor -= valor

    def exibir_saldo(self):
        print("="*20)
        print(f"Dono: {self.nome}\nSaldo: {self.get_valor()}")
        print("="*20)


nomeInserido = input("Nome:")

cofre = Cofre(0, nomeInserido)
cofre.depositar(100)
cofre.retirar(200)
cofre.exibir_saldo()




