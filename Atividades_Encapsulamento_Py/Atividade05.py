class Relogio:
    def __init__(self, horas, minutos, segundos):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def set_hora(self, hora, minuto, segundo):
        if(hora >= 0 and hora <= 24 and minuto >= 0 and minuto < 60 and segundo >= 0 and segundo < 60):
            self.__horas = hora
            self.__minutos = minuto
            self.__segundos = segundo
            print("Valores alterados com sucesso!")
        else:
            print("Valores inválidos!")

    def get_hora(self):
        return f"{self.__horas:02}:{self.__minutos:02}:{self.__segundos:02}"

    def avancar_segundo(self):
        self.__segundos += 1

        if self.__segundos > 59:
            self.__segundos = 0
            self.__minutos += 1

        if self.__minutos > 59:
            self.__minutos = 0
            self.__horas += 1

        if self.__horas > 23:
            self.__horas = 0

horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

relogio = Relogio(horas, minutos, segundos)

print("\nHorário inicial:")
print(relogio.get_hora())

print("\nTeste: alterar para 15:30:45")
relogio.set_hora(15, 30, 45)
print(relogio.get_hora())

print("\nTeste: alterar para 25:70:90")
relogio.set_hora(25, 70, 90)
print(relogio.get_hora())

print("\nTeste: avançar um segundo")
relogio.avancar_segundo()
print(relogio.get_hora())

print("\nTeste: 10:20:59 -> 10:21:00")
relogio.set_hora(10, 20, 59)
relogio.avancar_segundo()
print(relogio.get_hora())

print("\nTeste: 10:59:59 -> 11:00:00")
relogio.set_hora(10, 59, 59)
relogio.avancar_segundo()
print(relogio.get_hora())

print("\nTeste: 23:59:59 -> 00:00:00")
relogio.set_hora(23, 59, 59)
relogio.avancar_segundo()
print(relogio.get_hora())





