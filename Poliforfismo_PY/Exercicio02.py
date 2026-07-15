class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome}.")


class Recepcionista(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        print(f"Bem-vindo(a)! Meu nome é {self.nome}, posso ajudar?")


class Gerente(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        print(f"Olá! Sou {self.nome}, gerente desta unidade.")


class Tecnico(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        print(f"Oi, sou {self.nome}, do suporte técnico.")


funcionarios = [
    Recepcionista("Ana"),
    Recepcionista("Mariana"),
    Gerente("Carlos"),
    Gerente("Fernanda"),
    Tecnico("João"),
    Tecnico("Pedro")
]

for funcionario in funcionarios:
    funcionario.cumprimentar()