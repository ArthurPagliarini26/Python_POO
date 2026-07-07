class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

    def exibir_info(self):
        print("="*20)
        print("Largura: ", self.largura)
        print("Altura: ", self.altura)
        print("Área: ", self.calcular_area())
        print("Perímetro: ", self.calcular_perimetro())

largura = float(input("Largura: "))
altura = float(input("Altura: "))

retangulo = Retangulo(largura, altura)
retangulo.exibir_info()

largura = float(input("\nLargura: "))
altura = float(input("Altura: "))

retangulo2 = Retangulo(largura, altura)
retangulo2.exibir_info()