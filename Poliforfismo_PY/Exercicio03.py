class Lampada:
    def __init__(self, marca):
        self.marca = marca

    def acender(self):
        print(f"Lâmpada {self.marca} acendendo...")


class LampadaIncandescente(Lampada):
    def __init__(self, marca):
        super().__init__(marca)

    def acender(self):
        print(f"{self.marca}: Luz quente e amarelada acesa.")


class LampadaFluorescente(Lampada):
    def __init__(self, marca):
        super().__init__(marca)

    def acender(self):
        print(f"{self.marca}: Luz branca fria acesa.")


class LampadaLED(Lampada):
    def __init__(self, marca):
        super().__init__(marca)

    def acender(self):
        print(f"{self.marca}: Luz LED de baixo consumo acesa.")


def ligar_lampadas(lista):
    for lampada in lista:
        lampada.acender()

lampadas = [
    LampadaIncandescente("Philips"),
    LampadaIncandescente("Osram"),
    LampadaFluorescente("Elgin"),
    LampadaFluorescente("Avant"),
    LampadaLED("Intelbras"),
    LampadaLED("Ourolux")
]

ligar_lampadas(lampadas)