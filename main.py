from mesa import Mesa
from baralho import Baralho
from render import Render
from game import GameRules
from src.jogos import Truco

# Objects
baralho = Baralho(Truco)
mesa = Mesa()
game = GameRules(mesa.retornar_equipes())
render = Render(mesa, game)

# Inscritos
baralho.inscrever(game.receber_vira)
baralho.inscrever(mesa.distribuir_cartas)
mesa.inscrever(game.nova_carta_na_mesa)
mesa.inscrever(render.tela_de_jogadas)
mesa.inscrever(render.tela_de_acoes)

# Jogo
def iniciar_jogo():
    mesa.preencher_jogadores()
    mesa.formar_times()
    baralho.criar_baralho()
    while not game.have_game_winner():
        render.limpar(1)
        mesa.iniciar_mao()
        game.clear_round()
        baralho.pegar_baralho()
        baralho.enviar_cartas()
        baralho.enviar_vira()
        while not game.have_hand_winner():
            mesa.iniciar_rodada(game.rodada)
            game.have_round_winner()
            render.limpar(5)

iniciar_jogo()