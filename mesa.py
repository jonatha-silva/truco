import random
from jogador import Jogador
from equipe import Equipe

class Mesa:
    def __init__(self):
        self.estado = dict(observadores=[])
        self.__jogadores = []
        self.__equipes = []
        self.__cartas_na_mesa = []

    def inscrever(self, observador):
        self.estado['observadores'].append(observador)

    def notificar(self, comando):
        for observador in self.estado['observadores']:
            observador(comando)

    def preencher_jogadores(self):
        self.__jogadores.extend([
            Jogador('Jonatha', 1),
            Jogador('Pedro'),
            Jogador('Letícia'),
            Jogador('João')
        ])

    def formar_times(self):
        self.__equipes.extend([
            Equipe('Seu time', self.__jogadores[:2]),
            Equipe('Time Adversário', self.__jogadores[2:])
        ])
        for equipe in self.__equipes:
            equipe.estampar_equipe()
            equipe.reorganizar_integrantes()
        random.shuffle(self.__equipes)

    def iniciar_mao(self):
        for jogador in self.__jogadores:
            jogador.soltar_cartas()
        for equipes in self.__equipes:
            equipes.limpar_vitoria('rodadas')

    def distribuir_cartas(self, comando):
        if comando['evento'] == 'Dando as cartas':
            ordem = comando['ordem']
            self.__jogadores[ordem].receber_carta(comando['carta'])

    def iniciar_rodada(self, rodada):
        self.__cartas_na_mesa = []
        self.__solicitar_acao(rodada)

    def __solicitar_acao(self, rodada):
        primeiro = True
        for integrante in range(2):
            for equipe in self.__equipes:
                jogador = equipe.mostrar_integrante(integrante)                
                if jogador.jogavel == 1:
                    comando = dict(
                        evento="tela de ações",
                        rodada=rodada,
                        cartas=jogador.mostrar_cartas(),
                        primeiro=primeiro
                    )
                    self.notificar(comando)
                    escolha = jogador.selecionar_acao(rodada)
                else:
                    escolha = dict(acao="jogar", carta=0)
                self.__executar_acao(equipe, jogador, escolha)
            primeiro = False

    def __executar_acao(self, equipe, jogador, escolha):
        carta = jogador.retornar_carta(escolha['carta'])
        comando = dict(
            evento='nova carta na mesa',
            equipe=equipe,
            jogador=jogador,
            carta=carta,    
            estado=escolha['acao']
        )
        self.__adicionar_cartas_na_mesa(comando)
        self.notificar(comando)

    def __adicionar_cartas_na_mesa(self, comando:dict):
        self.__cartas_na_mesa.append(dict(
            jogador=comando['jogador'],
            carta=comando['carta'],
            estado=comando['estado']
        ))
        comando = dict(
            evento="cartas na mesa",
            jogadas=self.__cartas_na_mesa
        )
        self.notificar(comando)
        
    def retornar_equipes(self):
        return self.__equipes

    def equipe(self, equipe:int):
        return self.__equipes[equipe]