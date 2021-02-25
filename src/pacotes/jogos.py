from enum import IntEnum

class Truco:
    
    class naipes(IntEnum):
        Ouros = 1
        Espadas = 2
        Copas = 3
        Paus = 4

    class posicoes(IntEnum):
        Quatro = 1
        Cinco = 2
        Seis = 3
        Sete = 4
        Dama = 5
        Valete = 6
        Reis = 7
        Ás = 8
        Dois = 9

    def GerarCartas(self):
        naipes = list(Truco.naipes)
        posicoes = list(Truco.posicoes)
        return naipes, posicoes

    @property
    def qtCartas(self):
        return 3

    @property
    def qtJogadores(self):
        return 4

    def info(self):
        return "Truco!"