import random

class Teams:
    def __init__(self):
        self.state = {'observers':[]}
        self.doubles = []

# Subject Functions

    def init(self):
        self.clean_hands()

    def subscribe(self, observer_function):
        self.state['observers'].append(observer_function)
    
    def notify(self, command):
        for observer_function in self.state['observers']:
            observer_function(command)
    
    def listener(self, command):
        if command['event'] == 'players completed':
            players = command['players']
            self.take_players(players)
            
# class Functions

    def take_players(self, players):
        team_a = players[:2]
        team_b = players[2:]
        random.shuffle(team_a)
        random.shuffle(team_b)
        self.doubles.append(self.Team('Seu time', team_a))
        self.doubles.append(self.Team('Adversário', team_b))
        random.shuffle(self.doubles)
        for team in self.doubles:
            for player in team.players:
                player.name = f'{player.name} ({team.name.upper()})'

    def clean_rounds(self):
        self.rounds = 0
        self.ties = 0
            
    def clean_hands(self):
        for team in self.doubles:
            team.won['hands'] = 0

    def player_turn(self):
        for i in range(2):
            for team in self.doubles:
                player = team.players[i]
                choice = player.select_choice()
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