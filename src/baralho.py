import random

class Baralho:

    def __init__(self, jogo):
        self._jogo = jogo()
        self._cartas = []
        self.baralho = []
        self.estado = dict(observadores=[])

    def inscrever(self, observador):
        self.estado['observadores'].append(observador)

    def notificar(self, command):
        for observer_function in self.estado['observadores']:
            observer_function(command)

    def criar_baralho(self):
        valores = self._jogo.GerarCartas()
        for naipe in valores[0]:
            for posicao in valores[1]:
                carta = self.Carta(posicao, naipe)
                self._cartas.append(carta)

    def pegar_baralho(self):
        self.baralho = list(self._cartas)

    def pegar_carta(self):
        if len(self.baralho) > 0:
            carta_aleatoria = random.randint(0, len(self.baralho)-1)
            return self.baralho.pop(carta_aleatoria)
        else:
            print("Não há cartas suficientes no baralho, EMBARALHE!")

    def enviar_cartas(self):       
        for _ in range(self._jogo.qtCartas):
            for i in range(self._jogo.qtJogadores):
                carta = self.pegar_carta()
                command = {'evento':'Dando as cartas', 'ordem': i, 'carta':carta}
                self.notificar(command)

    def enviar_vira(self):
        vira = self.pegar_carta()
        i = self._cartas.index(vira)
        manilhas = self._cartas[i-1].posicao
        command = {'evento':'Vira', 'vira':vira, 'manilhas':manilhas}
        self.notificar(command)

    def __str__(self):
        return self._jogo.info()

    class Carta:
        def __init__(self, posicao, naipe):
            self.posicao = posicao
            self.naipe = naipe
            self.nome = f'{posicao.name} de {naipe.name}'