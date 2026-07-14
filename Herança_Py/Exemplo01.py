#pai
class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def exibir_info(self):
        print("="*20)
        print(f"Nome: {self.nome}\nSalário: {self.calcular_salario():.2f}")
        print("="*20)

#filhas
class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comissao):
        super().__init__(nome, salario_base)
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario_base + self.comissao

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.bonus + self.salario_base

#uso
funcionario = Funcionario("Juan", 1000)
vendedor = Vendedor("Maria", 3000, 500)
gerente = Gerente("Pedro", 4000, 3000)

funcionario.exibir_info()
vendedor.exibir_info()
gerente.exibir_info()


