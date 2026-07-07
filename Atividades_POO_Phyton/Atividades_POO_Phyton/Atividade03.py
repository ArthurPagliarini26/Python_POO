class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelecar(self):
        acelerada = int(input("Velocidade a acelerar: "))

        if(acelerada <= 0):
            print("Valor de aceleração inválido.")
        else:
            self.velocidade += acelerada

    def frear(self):
        freada = int(input("Velocidade a frear: "))

        if (freada > self.velocidade):
            print("Valor de freada inválido. A velocidade não pode ficar abaixo de 0.")
        else:
            self.velocidade -= freada

    def exibir_status(self):

        print("="*20)
        print(f"Carro: {self.marca} {self.modelo}({self.ano}) | Velocidade atual: {self.velocidade}km/h")
        print("="*20)


marca = input("Marca: ")
modelo = input("Modelo: ")
ano = int(input("Ano: "))

carro = Carro(marca, modelo, ano, 0)

while(True):
    print("="*20)
    print("1 - Acelerar")
    print("2 - Frear")
    print("3 - Exibir")
    print("0 - Sair")
    opcao = input("Opção: ")

    if(opcao == "1"):
        carro.acelecar()

    elif(opcao == "2"):
        carro.frear()

    elif(opcao == "3"):
        carro.exibir_status()

    elif(opcao == "0"):
        print("Saindo...")
        break



