class Turma:
    def __init__(self, nome, alunos):
        self.nome = nome
        self.alunos = []

    def matricular(self):
        nome = input("Nome: ")

        if(nome in self.alunos):
            print("Esse nome ja esta cadastrado!")
        else:
            self.alunos.append(nome)

    def remover(self):
        nome = input("Nome: ")

        if(nome in self.alunos):
            self.alunos.remove(nome)
        else:
            print("Esse nome nao esta cadastrado!")

    def listar(self):

        cont = 0
        for aluno in sorted(self.alunos):
            print(aluno)
            cont+=1
        print("Quantidade de alunos: ", cont)

    def esta_matriculado(self):
        nome = input("Nome: ")

        if(nome in self.alunos):
            print("Sim!")
            return True
        else:
            print("Não!")
            return False

nome = input("Digite o nome da turma: ")

turma = Turma(nome, [])

while(True):
    print("=" * 20)
    print("1 - Matricular")
    print("2 - Remover")
    print("3 - Listar")
    print("4 - Buscar")
    print("0 - Sair")
    opcao = input("Opção: ")

    if(opcao == "1"):
        turma.matricular()
    elif(opcao == "2"):
        turma.remover()
    elif(opcao == "3"):
        turma.listar()
    elif(opcao == "4"):
        turma.esta_matriculado()
    elif(opcao == "0"):
        print("Saindo...")
        break

