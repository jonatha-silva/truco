import random

class Teams:
    def __init__(self):
        self.doubles = []
           
# class Functions
    def clean_rounds(self):
        self.rounds = 0
        self.ties = 0

    def player_turn(self, rodada):
        for i in range(2):
            for team in self.doubles:
                player = team.players[i]
                choice = player.select_choice(rodada)
                carta = player.cards[choice['card']]
                
                if choice['action'] == 'play':
                    print(f" > {player.name} jogou a carta {carta.nome}.")
                    command = {
                        'event': 'player card',
                        'card': carta,
                        'player': player,
                        'team': team
                    }
                    self.notify(command)

                elif choice['action'] == 'hide':
                    print(f' > {player.name} escondeu a carta.')

                player.pop_card(choice['card'])
  
# Classs Objects

    class Team:
        def __init__(self, team_name, players):
            self.name = team_name
            self.players = players
            self.won = {
                'games': 0,
                'hands': 0,
                'rounds': 0
            }