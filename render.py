import time
import os

class Render:
    def __init__(self, mesa, game):
        self.__mesa = mesa
        self.__game = game

    def limpar(self, time_value=1):
        time.sleep(time_value)
        os.system('cls' if os.name == 'nt' else 'clear')

    def tela_inicial(self):
        print("-----------------------------------------------")
        print(f" Mãos: {self.__mesa.equipe(0).nome} ({self.__mesa.equipe(0).mostrar_vitorias('mãos')} x {self.__mesa.equipe(1).mostrar_vitorias('mãos')}) {self.__mesa.equipe(1).nome}")
        print(f" Rodadas: {self.__mesa.equipe(0).nome} ({self.__mesa.equipe(0).mostrar_vitorias('rodadas')} x {self.__mesa.equipe(1).mostrar_vitorias('rodadas')}) {self.__mesa.equipe(1).nome}")
        print(f" Rodada atual: {self.__game.round}")
        if self.__game.vira != None:
            print(f" Vira: {self.__game.vira.nome}")
        print("-----------------------------------------------\n")

    def tela_de_acoes(self, comando):
        if comando['evento'] == 'tela de ações':
            if comando['primeiro'] == True:
                self.tela_inicial()
            print("\n-----------------------------------------------")
            for carta in enumerate(comando['cartas']):
                print(f"Opção {carta[0]+1 }: {carta[1].nome}")
            print('')
            if comando['rodada'] > 1:
                print(f'Opção 8: Esconder')
            print(f'Opção 9: Truco!')
            print("-----------------------------------------------\n")

    def tela_de_jogadas(self, comando):
        if comando['evento'] == 'cartas na mesa':
            self.limpar(1)
            self.tela_inicial()
            for jogada in comando['jogadas']:
                if jogada['estado'] == 'jogar':
                    print(f" > {jogada['jogador'].nome} jogou a carta {jogada['carta'].nome}.")
                else:
                    print(f" > {jogada['jogador'].nome} escondeu a carta.")