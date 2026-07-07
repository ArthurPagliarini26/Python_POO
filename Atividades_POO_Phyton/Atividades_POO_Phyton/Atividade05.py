class Calculadora:

    def __init__(self, historico):
        self.historico = []

    def somar(self):
        a = int(input("Digite o valor do numero A: "))
        b = int(input("Digite o valor do numero B: "))

        soma = a + b
        guardar = f"{a} + {b} = {soma}"

        self.historico.append(guardar)
        return soma

    def subtrair(self):
        a = int(input("Digite o valor do numero A: "))
        b = int(input("Digite o valor do numero B: "))

        subtracao = a - b
        guardar = f"{a} - {b} = {subtracao}"

        self.historico.append(guardar)
        return subtracao

    def multiplicar(self):
        a = int(input("Digite o valor do numero A: "))
        b = int(input("Digite o valor do numero B: "))

        multiplicacao = a * b
        guardar = f"{a} * {b} = {multiplicacao}"

        self.historico.append(guardar)
        return multiplicacao

    def dividir(self):
        a = int(input("Digite o valor do numero A: "))
        b = int(input("Digite o valor do numero B: "))

        if(b == 0):
            print("Proibido!")
        else:
            divisao = a / b
            guardar = f"{a} / {b} = {divisao}"

            self.historico.append(guardar)
            return divisao

    def exibir_dados(self):
     if not self.historico:
        print("Lista vazia!")
     else:
        print("="*20)
        for historico in self.historico:
            print(historico)
        print("="*20)

historico = Calculadora("Histórico: ")

while(True):
    print("=" * 20)
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Exibir")
    print("0 - Sair")
    opcao = input("Opção: ")

    if(opcao == "1"):
        print("Resultado: ", historico.somar())
    elif(opcao == "2"):
        print("Resultado: ", historico.subtrair())
    elif(opcao == "3"):
        print("Resultado: ", historico.multiplicar())
    elif(opcao == "4"):
        print("Resultado: ", historico.dividir())
    elif(opcao == "5"):
        print("Resultados: ")
        historico.exibir_dados()
    elif(opcao == "0"):
        print("Saindo...")
        break






