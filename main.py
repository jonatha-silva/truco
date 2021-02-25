import os
import time
from src.baralho import Baralho
from src.pacotes.jogos import Truco
from players import Players
from teams import Teams
from game import GameRules

def clear_output(time_value):
    time.sleep(time_value)
    os.system('cls' if os.name == 'nt' else 'clear')

# Objects
players = Players()
teams = Teams()
game = GameRules(teams.doubles)
baralho = Baralho(Truco)

# Subscribes
players.subscribe(teams.listener)
baralho.observer_subscribe(game.receberVira)
baralho.observer_subscribe(players.receberCartas)
teams.subscribe(game.listener)

# Game
def start_game():
    players.init()
    teams.init()
    baralho.CriarBaralho()
    while not game.have_game_winner():
        clear_output(1)
        players.clean_cards()
        game.clear_round()
        baralho.pegarBaralho()
        baralho.enviarCartas()
        baralho.enviarVira()
        while not game.have_hand_winner():
            clear_output(1)
            game.show_info()
            teams.player_turn()
            game.have_round_winner()
            clear_output(5)

start_game()