class Transporte:
    def __init__(self, nome):
        self.nome = nome

    def viajar(self):
        print("Viajando...")

class Aviao(Transporte):
    def __init__(self, nome):
        super().__init__(nome)

    def viajar(self):
        print("Voando de avião...")

class Navio(Transporte):
    def __init__(self, nome):
        super().__init__(nome)

    def viajar(self):
        print(f"{self.nome} está navegando de navio...")


class Trem(Transporte):
    def __init__(self, nome):
        super().__init__(nome)

    def viajar(self):
        print(f"{self.nome} está viajando de trem...")

aviao = Aviao("Boeing 737")
navio = Navio("Titanic")
trem = Trem("Expresso do Oriente")

aviao.viajar()
navio.viajar()
trem.viajar()