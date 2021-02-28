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

    def inscrever(self, observer_function):
        self.state['observers'].append(observer_function)

    def notificar(self, command):
        for observer_function in self.state['observers']:
            observer_function(command)

# Apresentação

    @property
    def rodada(self):
        return self.round

# Limpeza de informações

    def clear_table(self):
        self.vira = None

    def clear_round(self):
        self.round = 1
        self.tie = 0

    def receber_vira(self, comando):
        if comando['evento'] == 'Vira':
            self.manilhas = comando['manilhas']
            self.vira = comando['vira']

# Verificação de melhor carta

    def verificar_carta(self, comando):

        if comando['evento'] == 'carta de jogador':
            carta = comando['carta']
            jogador = comando['jogador']
            equipe = comando['equipe']

        # Put my card if don't have card in the table
        if self.maiorCarta == None:
            self.win_or_tie(carta, jogador, equipe, 'winner')
        
        # If my card is a Joker...
        elif carta.posicao == self.manilhas:
            
            # And have another joker in the table...
            if self.maiorCarta.posicao == self.manilhas:
                
                # Put my card if my suit is better.
                if carta.naipe > self.maiorCarta.naipe:
                    self.win_or_tie(carta, jogador, equipe, 'winner')
            
            # If there is no other joker on the table, put my card.
            else:
                self.win_or_tie(carta, jogador, equipe, 'winner')

        # If my is not a joker...
        elif self.maiorCarta.posicao != self.manilhas:

            # Put on the table, if my card value is better than card value on the table.
            if carta.posicao > self.maiorCarta.posicao:
                self.win_or_tie(carta, jogador, equipe, 'winner')

            # If my card is the same as the card on the table and the card is not from my teammate, I declare a tie.
            elif carta.posicao == self.maiorCarta.posicao and equipe != self.card_of_team:
                self.win_or_tie(carta, jogador, equipe, 'tie')

    def win_or_tie(self, carta, jogador, equipe, evento):
        if evento == 'winner':
            self.maiorCarta = carta
            self.card_of_team = equipe
            self.card_of_player = jogador
        elif evento == 'tie':
            self.maiorCarta = carta
            self.card_of_team = None
            self.card_of_player = None       

# Verificação de vitória

    def have_round_winner(self):

        if self.maiorCarta.posicao == self.manilhas:
            print(f"\n * Nesta rodada, {self.card_of_player.nome} venceu com a manilha: {self.maiorCarta.nome}.\n")
            self.card_of_team.adicionar_vitoria('rodadas', 1)

        elif self.card_of_player != None:
            print(f"\n * Nesta rodada, a carta mais forte é a {self.maiorCarta.nome} de {self.card_of_player.nome}.\n")
            self.card_of_team.adicionar_vitoria('rodadas', 1)

        else:
            print(f"\n * Houve um empate com {self.maiorCarta.nome}.\n")
            self.tie += 1
        
        self.maiorCarta = None
        self.round += 1

    def have_hand_winner(self):
        hand_winner = []

        if self.tie == 0:
            hand_winner = [team for team in self.doubles if team.mostrar_vitorias('rodadas') >= 2]
              
        elif self.round >= 2 and self.tie >= 1:
            hand_winner = [team for team in self.doubles if team.mostrar_vitorias('rodadas') == 1]

        elif self.round == 3 and self.tie == 3:
            print(f"Hand tied.\n")
            return True
        
        if len(hand_winner) > 0:
            hand_winner[0].adicionar_vitoria('mãos', 1)
            print(f"{hand_winner[0].nome} venceu a mão.\n")
            return True
        return False

    def have_game_winner(self):
        game_winner = [team for team in self.doubles if team.mostrar_vitorias('mãos') >= 3]
        if len(game_winner) > 0 and game_winner[0].nome == 'Seu time':
            game_winner[0].adicionar_vitoria('jogos', 1)
            print(f"\nParabéns! {game_winner[0].nome} venceu o jogo.\n")
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
        elif len(game_winner) > 0 and game_winner[0].nome != 'Seu time':
            print("Não foi dessa vez, o adversario venceu!")
            print("    _______________         ")
            print("   /               \        ")
            print("  /                 \       ")
            print("//                   \/\    ")
            print("\|   XXXX     XXXX   | /    ")
            print(" |   XXXX     XXXX   |/     ")
            print(" |   XXX       XXX   |      ")
            print(" |                   |      ")
            print(" \__      XXX      __/      ")
            print("   |\     XXX     /|        ")
            print("   | |           | |        ")
            print("   | I I I I I I I |        ")
            print("   |  I I I I I I  |        ")
            print("   \_             _/        ")
            print("     \_         _/          ")
            print("       \_______/            ")
            return True
        return False