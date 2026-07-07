class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    def set_senha(self, novaSenha):
        if(len(novaSenha) >= 6):
            self.__senha = novaSenha
            print("Senha alterada com sucesso!")
        else:
            print("Senha invalida!")

    def verificar_senha(self, senhaDigitada):
        if(senhaDigitada == self.get_senha()):
            return True
        else:
            return False

    def exibir_perfil(self):
        print("=" * 20)
        print(f"Nome: {self.nome}\nEmail: {self.email}\n Senha: {"*" * len(self.get_senha())}")
        print("=" * 20)

nomeInserido = input("Nome: ")
emailInserido = input("Email: ")
senhaInserida = input("Senha: ")

usuario = Usuario(nomeInserido, emailInserido, senhaInserida)

usuario.set_senha("43573453456")

verificar = input("Senha:")
verificado = usuario.verificar_senha(verificar)
if(verificado):
    print("Senha valida!")
else:
    print("Senha invalida!")


