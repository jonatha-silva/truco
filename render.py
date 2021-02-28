class Render:
    def __init__(self, mesa, game):
        self.__mesa = mesa
        self.__game = game

    def apresentar_infos(self):
        print("-----------------------------------------------")
        print(f" Mãos: {self.__mesa.equipe(0).nome} ({self.__mesa.equipe(0).mostrar_vitorias('mãos')} x {self.__mesa.equipe(1).mostrar_vitorias('mãos')}) {self.__mesa.equipe(1).nome}")
        print(f" Rodadas: {self.__mesa.equipe(0).nome} ({self.__mesa.equipe(0).mostrar_vitorias('rodadas')} x {self.__mesa.equipe(1).mostrar_vitorias('rodadas')}) {self.__mesa.equipe(1).nome}")
        print(f" Rodada atual: {self.__game.round}")
        if self.__game.vira != None:
            print(f" Vira: {self.__game.vira.nome}")
        print("-----------------------------------------------\n")