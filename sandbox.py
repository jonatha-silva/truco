from src.baralho import Baralho
from src.pacotes.jogos import Truco
from src.pacotes.jogos import Blackjack
from src.pacotes.jogos import Poker

baralho = Baralho(Truco)
baralho.CriarBaralho()
baralho.pegarBaralho()
cartas = baralho.darCartas()

print(baralho)
for carta in cartas:
    print(carta['nome'])