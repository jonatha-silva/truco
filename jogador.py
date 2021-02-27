class Jogador:
    def __init__(self, nome, jogavel=0):
        self.__nome = nome
        self.__cartas = []
        self.__jogavel = jogavel
        self.estado = dict(observadores=[])

    def inscrever(self, observador):
        self.estado['observadores'].append(observador)

    def notificar(self, comando):
        for observador in self.estado['observadores']:
            observador(comando)

    @property
    def nome(self):
        return self.__nome

    def soltar_cartas(self):
        self.__cartas = []

    def receber_carta(self, carta):
        self.__cartas.append(carta)

    def ver_carta(self, carta):
        return self.__cartas[carta]

    def enviar_carta(self, carta):
        return self.__cartas.pop(carta)

    def selecionar_acao(self, rodada):
        if len(self.__cartas) == 0:
            print("O jogador não tem cartas para escolher.")
            return False
        elif self.__jogavel == 1:
            self.__mostrar_acoes(rodada)            
            escolha_valida = False
            while not escolha_valida:
                decisao:int = self.__tomar_decisao()
                escolha = self.__validar_escolha(decisao, rodada)
                escolha_valida = escolha != False
        else:
            escolha = dict(acao="jogar", carta=0)
        return escolha

    def __mostrar_acoes(self, rodada):
        print("\n-----------------------------------------------")
        for index, carta in zip(range(len(self.__cartas)), self.__cartas):
            print(f"Opção {index + 1 }: {carta.__nome}")
        print('')
        if rodada > 1:
            print(f'Opção 8: Esconder')
        print(f'Opção 9: Truco!')
        print("-----------------------------------------------\n")

    def __tomar_decisao(self, acao='Jogar') -> int:
        if acao == 'esconder':
            texto = f"{self.__nome} Selecione uma carta para esconder: "
        else:
            texto = f"{self.__nome} Selecione uma carta ou ação: "
        
        while True:
            try:
                escolha:int = int(input(texto))
            except:
                print("Não foi possível registrar sua escolha.")
            else:
                return escolha

    def __validar_escolha(self, escolha, rodada):
        if escolha-1 in range(len(self.__cartas)):
            return dict(acao='jogar', carta=escolha-1)
        elif escolha == 9:
            return dict(acao='truco')
        elif escolha == 8 and rodada > 1:
            escolha:int = self.__tomar_decisao(acao='esconder')
            if escolha-1 in range(len(self.__cartas)):
                return dict(acao='esconder', carta=escolha-1)
        else:
            return False