class Termostato:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, valor):
        if(valor >= 16 and valor <= 30):
            self.__temperatura = valor
        else:
            print("Valor invalido")

    def exibir_status(self):
        print("="*20)
        print(f"Temperatura atual: {self.get_temperatura()}")
        print("="*20)

temperaturaAtual = int(input("Informe o temperatura atual: "))

termostato = Termostato(temperaturaAtual)

termostato.set_temperatura(30)
termostato.exibir_status()

termostato.set_temperatura(2)
termostato.exibir_status()
