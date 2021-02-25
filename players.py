import random

class Players:

    def __init__(self):
        self.state = {'observers':[]}
        self.players = []

    def init(self):
        self.add_player()
        self.fill_players()
        self.set_teams()

# Subject Functions

    def subscribe(self, observer_function):
        self.state['observers'].append(observer_function)

    def notify(self, command):
        for observer_function in self.state['observers']:
            observer_function(command)
                                
# Class Functions

    def add_player(self):
        if len(self.players) < 4:
            player_name = input("Insira seu nome: ")
            self.players.append(self.Player(player_name, 1))
        else:                        
            print("O número de jogadores foi excedido.")

    def fill_players(self):
        number_of_bots = 4 - len(self.players)
        for i in range(number_of_bots):        
            self.players.append(self.Player(f'Player {i + 1}', 0))

    def set_teams(self):
        random.shuffle(self.players)
        command = {
            'event':'players completed',
            'players': self.players
        }
        self.notify(command)

    def remove_player(self):
        try:
            self.show_players()
            player_to_remove = int(input("Selecione um jogador para remover."))-1
            del(self.players[player_to_remove])
        except:
            print("Não entend sua escolha.")

    def show_players(self):
        if len(self.players) > 0:
            print("\n Jogador\n----------------------")        
            [print(f" > {player.name}") for player in self.players]
        else:
            print("Não existem jogadores.")

    def receberCartas(self, command):
        if command['evento'] == 'Dando as cartas':
            i = command['ordem']
            self.players[i].cards.append(command['carta'])

    def clean_cards(self):
        for player in self.players:
            player.cards = []

# Classs Objects

    class Player():
        def __init__(self, player_name, playable):
            self.name = player_name
            self.cards = []
            self.playable = playable


        def select_choice(self):
            if self.playable == 1:
                self.show_choices()
                
                valid_choice = False

                while not valid_choice:
                    your_choice = int(input(f"{self.name} Selecione uma carta ou ação: "))

                    if your_choice-1 in range(len(self.cards)):
                        choice = {'action': 'play', 'card': your_choice-1}

                    elif your_choice == 9:
                        print("Truco!")

                    elif your_choice == 8:
                        print("Hide card!")
                        your_choice = int(input(f"{self.name} Selecione uma carta para esconder: "))
                        
                        if your_choice-1 in range(len(self.cards)):
                            choice = {'action': 'hide', 'card': your_choice-1}

                    else:
                        print("Comando inválido.")

                    valid_choice = your_choice-1 in range(len(self.cards))

            else:
                choice = {'action': 'play', 'card': 0}
            
            return choice
            
        def show_choices(self):
            print("\n-----------------------------------------------")
            for index, card in zip(range(len(self.cards)), self.cards):
                print(f"Opção {index + 1 }: {card.nome}")
            print('')
            print(f'Opção 8: Esconder')
            print(f'Opção 9: Truco!')
            print("-----------------------------------------------\n")

        def pop_card(self, card):
            return self.cards.pop(card)