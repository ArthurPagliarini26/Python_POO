import math


class Forma:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def calcular_area(self):
        pass

    def exibir_info(self):
        print(f"O {self.nome} de cor {self.cor} tem ")

class Circulo(Forma):
    def __init__(self, nome, cor, raio):
        super().__init__(nome, cor)
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio**2

    def exibir_info(self):
        super().exibir_info()
        print(f"Área: {self.calcular_area():.2f} cm²")

class Retangulo(Forma):
    def __init__(self, nome, cor, base, altura):
        super().__init__(nome, cor)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def exibir_info(self):
        super().exibir_info()
        print(f"Área: {self.calcular_area():.2f} cm²")

class Triangulo(Forma):
    def __init__(self, nome, cor, base, altura):
        super().__init__(nome, cor)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def exibir_info(self):
        super().exibir_info()
        print(f"Área: {self.calcular_area():.2f} cm²")

circulo = Circulo("Círculo", "Azul", 5)
retangulo = Retangulo("Retângulo", "Vermelho", 10, 4)
triangulo = Triangulo("Triângulo", "Verde", 8, 6)

circulo.exibir_info()

retangulo.exibir_info()

triangulo.exibir_info()



