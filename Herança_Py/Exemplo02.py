class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print(f"{self.nome} faz barulho gerérico.")

    def mover(self):
        print(f"{self.nome} se move genericamente.")

    def exibir_info(self):
        print("="*20)
        print(f"{self.nome} tem {self.idade} anos.")
        print("="*20)

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print(f"{self.nome} late.")

    def mover(self):
        print(f"{self.nome} corre em 4 patas.")

    def exibir_info(self):
        print("=" * 20)
        print(f"{self.nome} tem {self.idade} anos e é da raça {self.raca}.")
        print("=" * 20)

class Passaro(Animal):
    def __init__(self, nome, idade, pode_voar):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar

    def emitir_som(self):
        print(f"{self.nome} assovia.")

    def mover(self):
        print(f"{self.nome} voa.")

    def exibir_info(self):
        print("=" * 20)
        print(f"{self.nome} tem {self.idade} anos e ele {"pode voar" if self.pode_voar else "não pode voar"}.")
        print("=" * 20)

animal = Animal("Genérico", 3)
cachorro = Cachorro("Cachorro", 8, "SRD")
passaro = Passaro("Passaro", 5, True)

animal.emitir_som()
animal.mover()
animal.exibir_info()

cachorro.emitir_som()
cachorro.mover()
cachorro.exibir_info()

passaro.emitir_som()
passaro.mover()
passaro.exibir_info()