from enum import IntEnum

class Truco:

    QNTD_CARTAS = 3
    QNTD_JOGADORES = 4
    
    class naipes(IntEnum):
        OUROS = 1
        ESPADAS = 2
        COPAS = 3
        PAUS = 4

    class posicoes(IntEnum):
        QUATRO = 1
        CINCO = 2
        SEIS = 3
        SETE = 4
        DAMA = 5
        VALETE = 6
        REIS = 7
        ÁS = 8
        DOIS = 9

    def GerarCartas(self):
        naipes = list(Truco.naipes)
        posicoes = list(Truco.posicoes)
        return naipes, posicoes
        
    def info(self):
        return "Cartas de truco."