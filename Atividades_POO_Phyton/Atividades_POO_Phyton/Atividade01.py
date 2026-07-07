class Pessoa:

    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def exibirDados(self):
        print("="*20)
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e moro em {cidade}")
        print("="*20)

nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")

pessoa = Pessoa(nome, idade, cidade)
pessoa.exibirDados()

nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")

pessoa2 = Pessoa(nome, idade, cidade)
pessoa2.exibirDados()

nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")

pessoa3 = Pessoa(nome, idade, cidade)
pessoa3.exibirDados()