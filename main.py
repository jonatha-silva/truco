import os
import time
from mesa import Mesa
from src.baralho import Baralho
from src.pacotes.jogos import Truco
from game import GameRules

def clear_output(time_value):
    time.sleep(time_value)
    os.system('cls' if os.name == 'nt' else 'clear')

# Objects
baralho = Baralho(Truco)
mesa = Mesa()
game = GameRules(mesa.retornar_equipes())

# Subscribes
baralho.inscrever(game.receber_vira)
baralho.inscrever(mesa.distribuir_cartas)
mesa.inscrever(game.verificar_carta)

# Game
def iniciar_jogo():
    mesa.preencher_jogadores()
    mesa.formar_times()
    baralho.criar_baralho()
    while not game.have_game_winner():
        clear_output(1)
        mesa.iniciar_mao()
        game.clear_round()
        baralho.pegar_baralho()
        baralho.enviar_cartas()
        baralho.enviar_vira()
        while not game.have_hand_winner():
            clear_output(1)
            game.show_info()
            mesa.iniciar_rodada()
            game.have_round_winner()
            clear_output(5)