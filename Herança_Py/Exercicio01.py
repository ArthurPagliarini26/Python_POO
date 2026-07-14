class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print("="*20)
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print("="*20)

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, rodas):
        super().__init__(marca, modelo, ano)
        self.rodas = rodas

    def exibir_info(self):
        print("=" * 20)
        super().exibir_info()
        print(f'Rodas: {self.rodas}')
        print("=" * 20)

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def exibir_info(self):
        print("=" * 20)
        super().exibir_info()
        print(f'Potência: {self.potencia}')
        print("=" * 20)

moto = Moto('Moto', 18, '2020', 2)
carro = Carro('Carro', 30, '2020', 3000)

moto.exibir_info()
carro.exibir_info()