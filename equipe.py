class Equipe:
    def __init__(self, nome:str, integrantes:list):
        self.__nome = nome
        self.__integrantes = integrantes
        self.__vitorias = {
                'jogos': 0,
                'mãos': 0,
                'rodadas': 0
            }

    @property
    def nome(self):
        return self.__nome

    def limpar_vitoria(self, vitoria:str):
        self.__vitorias[vitoria] = 0

    def mostrar_integrante(self, integrante):
        return self.__integrantes[integrante]

    def mostrar_vitorias(self, vitoria):
        return self.__vitorias[vitoria]

    def adicionar_vitoria(self, vitoria, pontos):
        self.__vitorias[vitoria] += pontos