import random

class Baralho:

    def __init__(self, jogo):
        self._jogo = jogo()
        self._cartas = []
        self.baralho = []
        self.estado = {
            'observers': []
        }

    def observer_subscribe(self, observer_function):
        self.estado['observers'].append(observer_function)

    def observer_notify(self, command):
        for observer_function in self.estado['observers']:
            observer_function(command)

    def CriarBaralho(self):
        valores = self._jogo.GerarCartas()
        for naipe in valores[0]:
            for posicao in valores[1]:
                carta = self.Carta(posicao, naipe)
                self._cartas.append(carta)

    def pegarBaralho(self):
        self.baralho = list(self._cartas)

    def pegarCarta(self):
        if len(self.baralho) > 0:
            carta_aleatoria = random.randint(0, len(self.baralho)-1)
            return self.baralho.pop(carta_aleatoria)
        else:
            print("Não há cartas suficientes no baralho, EMBARALHE!")

    def enviarCartas(self):       
        for _ in range(self._jogo.qtCartas):
            for i in range(self._jogo.qtJogadores):
                carta = self.pegarCarta()
                command = {'evento':'Dando as cartas', 'ordem': i, 'carta':carta}
                self.observer_notify(command)

    def enviarVira(self):
        vira = self.pegarCarta()
        i = self._cartas.index(vira)
        manilhas = self._cartas[i-1].posicao
        command = {'evento':'Vira', 'vira':vira, 'manilhas':manilhas}
        self.observer_notify(command)

    def __str__(self):
        return self._jogo.info()

    class Carta:
        def __init__(self, posicao, naipe):
            self.posicao = posicao
            self.naipe = naipe
            self.nome = f'{posicao.name} de {naipe.name}'