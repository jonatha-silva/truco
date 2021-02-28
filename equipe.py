import random

class Equipe:
    def __init__(self, nome:str, integrantes:list):
        self.__nome = nome
        self.__integrantes = integrantes
        self.__vitorias = dict(
                jogos = 0,
                mãos =  0,
                rodadas =  0
        )

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def limpar_vitoria(self, vitoria:str):
        self.__vitorias[vitoria] = 0

    def estampar_equipe(self):
        for jogador in self.__integrantes:
            jogador.estampar_equipe(self.__nome)

    def reorganizar_integrantes(self):
        random.shuffle(self.__integrantes)

    def mostrar_integrante(self, integrante):
        return self.__integrantes[integrante]

    def mostrar_vitorias(self, vitoria):
        return self.__vitorias[vitoria]

    def adicionar_vitoria(self, vitoria, pontos):
        self.__vitorias[vitoria] += pontos