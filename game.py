class GameRules:
    def __init__(self, doubles):
        self.state = {'observers':[]}
        self.manilhas = 0
        self.maiorCarta = None
        self.vira = {}
        self.card_of_team = None
        self.card_of_player = None
        self.tie = 0
        self.round = 1
        self.doubles = doubles

# Subject Functions

    def subscribe(self, observer_function):
        self.state['observers'].append(observer_function)

    def notify(self, command):
        for observer_function in self.state['observers']:
            observer_function(command)

    def listener(self, command):
        if command['event'] == 'player card':
            carta = command['card']
            jogador = command['player']
            time = command['team']
            self.evaluate_player_card(carta, jogador, time)

# Apresentação

    def show_info(self):
        print("-----------------------------------------------")
        print(f" Mãos: Time A ({self.doubles[0].won['hands']} x {self.doubles[1].won['hands']}) Time B")
        print(f" Rodadas: Time A ({self.doubles[0].won['rounds']} x {self.doubles[1].won['rounds']}) Time B")
        print(f" Rodada atual: {self.round}")
        if self.vira != None:
            print(f" Vira: {self.vira.nome}")
        print("-----------------------------------------------\n")

# Limpeza de informações

    def clear_table(self):
        self.vira = None

    def clear_round(self):
        self.round = 1
        self.tie = 0
        for double in self.doubles:
            double.won['rounds'] = 0

    def receberVira(self, command):
        if command['evento'] == 'Vira':
            self.manilhas = command['manilhas']
            self.vira = command['vira']

# Verificação de melhor carta

    def evaluate_player_card(self, carta, player, team):

        # Put my card if don't have card in the table
        if self.maiorCarta == None:
            self.win_or_tie(carta, player, team, 'winner')
        
        # If my card is a Joker...
        elif carta.posicao == self.manilhas:
            
            # And have another joker in the table...
            if self.maiorCarta.posicao == self.manilhas:
                
                # Put my card if my suit is better.
                if carta.naipe > self.maiorCarta.naipe:
                    self.win_or_tie(carta, player, team, 'winner')
            
            # If there is no other joker on the table, put my card.
            else:
                self.win_or_tie(carta, player, team, 'winner')

        # If my is not a joker...
        elif self.maiorCarta.posicao != self.manilhas:

            # Put on the table, if my card value is better than card value on the table.
            if carta.posicao > self.maiorCarta.posicao:
                self.win_or_tie(carta, player, team, 'winner')

            # If my card is the same as the card on the table and the card is not from my teammate, I declare a tie.
            elif carta.posicao == self.maiorCarta.posicao and team != self.card_of_team:
                self.win_or_tie(carta, player, team, 'tie')

    def win_or_tie(self, carta, player, team, event):
        if event == 'winner':
            self.maiorCarta = carta
            self.card_of_team = team
            self.card_of_player = player
        elif event == 'tie':
            self.maiorCarta = carta
            self.card_of_team = None
            self.card_of_player = None       

# Verificação de vitória

    def have_round_winner(self):

        if self.maiorCarta.posicao == self.manilhas:
            print(f"\n * Nesta rodada, {self.card_of_player.name} venceu com a manilha: {self.maiorCarta.nome}.\n")
            self.card_of_team.won['rounds'] += 1

        elif self.card_of_player != None:
            print(f"\n * Nesta rodada, a carta mais forte é a {self.maiorCarta.nome} de {self.card_of_player.name}.\n")
            self.card_of_team.won['rounds'] += 1

        else:
            print(f"\n * Houve um empate com {self.maiorCarta.nome}.\n")
            self.tie += 1
        
        self.maiorCarta = None
        self.round += 1

    def have_hand_winner(self):
        hand_winner = []

        if self.tie == 0:
            hand_winner = [team for team in self.doubles if team.won['rounds'] >= 2]
              
        elif self.round >= 2 and self.tie >= 1:
            hand_winner = [team for team in self.doubles if team.won['rounds'] == 1]

        elif self.round == 3 and self.tie == 3:
            print(f"Hand tied.\n")
            return True
        
        if len(hand_winner) > 0:
            hand_winner[0].won['hands'] += 1
            print(f"{hand_winner[0].name} venceu a mão.\n")
            return True
        return False

    def have_game_winner(self):
        game_winner = [team for team in self.doubles if team.won['hands'] >= 3]
        if len(game_winner) > 0:
            game_winner[0].won['games'] += 1
            print(f"\nParabéns! {game_winner[0].name} venceu o jogo.\n")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
            return True
        return False