import random
from jogador import Jogador
from equipe import Equipe

class Mesa:
    def __init__(self):
        self.__jogadores = []
        self.__equipes = []
        self.estado = dict(observadores=[])

    def inscrever(self, observador):
        self.estado['observadores'].append(observador)

    def notificar(self, comando):
        for observador in self.estado['observadores']:
            observador(comando)

    def preencher_jogadores(self):
        self.__jogadores.extend([
            Jogador('Você', 1),
            Jogador('Pedro'),
            Jogador('Letícia'),
            Jogador('João')
        ])

    def formar_times(self):
        random.shuffle(self.__jogadores)
        self.__equipes.extend([
            Equipe('Seu time', self.__jogadores[2:]),
            Equipe('Time Adversário', self.__jogadores[:2])
        ])

    def iniciar_mao(self):
        for jogador in self.__jogadores:
            jogador.soltar_cartas()
        for equipes in self.__equipes:
            equipes.limpar_vitoria('rodadas')

    def distribuir_cartas(self, comando):
        if comando['evento'] == 'Dando as cartas':
            ordem = comando['ordem']
            self.__jogadores[ordem].receber_carta(comando['carta'])

    def iniciar_rodada(self):
        for integrante in range(2):
            for equipe in self.__equipes:
                jogador = equipe.mostrar_integrante(integrante)
                escolha = jogador.selecionar_acao(1)
                carta = jogador.ver_carta(escolha['carta'])
                jogador.enviar_carta(carta)
                
                if escolha['acao'] == 'jogar':
                    print(f" > {jogador.nome} jogou a carta {carta.nome}.")
                    comando = dict(
                        evento='carta de jogador',
                        carta= carta,
                        jogador= jogador,
                        equipe= equipe
                    )
                    self.notificar(comando)

                elif escolha['acao'] == 'esconder':
                    print(f' > {jogador.nome} escondeu a carta.')

    def retornar_equipes(self):
        return self.__equipes