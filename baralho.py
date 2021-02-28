from carta import Carta
import random

class Baralho:

    def __init__(self, jogo):
        self.__estado = dict(observadores=[])
        self.__jogo = jogo()
        self.__cartas = []
        self.__baralho = []
    
    def inscrever(self, observador):
        self.__estado['observadores'].append(observador)

    def notificar(self, command):
        for observer_function in self.__estado['observadores']:
            observer_function(command)

    @property
    def baralho(self):
        return self.__baralho

    def criar_baralho(self):
        valores = self.__jogo.GerarCartas()
        for naipe in valores[0]:
            for posicao in valores[1]:
                carta = Carta(posicao, naipe)
                self.__cartas.append(carta)

    def pegar_baralho(self):
        self.__baralho = list(self.__cartas)

    def pegar_carta(self):
        if len(self.__baralho) > 0:
            carta_aleatoria = random.randint(0, len(self.__baralho)-1)
            return self.__baralho.pop(carta_aleatoria)
        else:
            print("Não há cartas suficientes no baralho, EMBARALHE!")

    def enviar_cartas(self):       
        for _ in range(self.__jogo.QNTD_CARTAS):
            for i in range(self.__jogo.QNTD_JOGADORES):
                carta = self.pegar_carta()
                command = {'evento':'Dando as cartas', 'ordem': i, 'carta':carta}
                self.notificar(command)

    def enviar_vira(self):
        vira = self.pegar_carta()
        i = self.__cartas.index(vira)
        manilhas = self.__cartas[i-1].posicao
        command = {'evento':'Vira', 'vira':vira, 'manilhas':manilhas}
        self.notificar(command)

    def __str__(self):
        return self.__jogo.info()