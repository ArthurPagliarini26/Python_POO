class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque

    def get_estoque(self):
        return self.__estoque

    def adiciona_estoque(self, quantidade):
        if(quantidade >= 0):
            self.__estoque += quantidade
            print("Estoque alterado com sucesso!")
        else:
            print("Erro: Valor inválido!")

    def vender(self, quantidade):
        if(quantidade > self.get_estoque()):
            print("Valor inválido!")
        else:
            self.__estoque -= quantidade
            print("Venda realizada com sucesso!")

    def exibir_info(self):
        print("=" * 20)
        print(f"Nome: {self.nome}\nPreço: {self.preco}\nEstoque atual: {self.get_estoque()}")
        print("=" * 20)

nome = input("Nome do produto: ")
preco = float(input("Preço: "))
estoque = int(input("Estoque inicial: "))

produto = Produto(nome, preco, estoque)

produto.exibir_info()

produto.adiciona_estoque(20)
produto.exibir_info()

produto.adiciona_estoque(-5)
produto.exibir_info()

produto.vender(10)
produto.exibir_info()

produto.vender(30)
produto.exibir_info()





