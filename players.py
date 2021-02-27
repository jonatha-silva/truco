import random

class Players:

    def __init__(self):
        self.players = []

    class Player():
        def __init__(self, player_name, playable):
            self.name = player_name
            self.cards = []
            self.playable = playable

        def pop_card(self, card):
            return self.cards.pop(card)