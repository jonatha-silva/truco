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

    @property
    def jogavel(self):
        return self.__jogavel

    def mostrar_cartas(self):
        return self.__cartas

    def soltar_cartas(self):
        self.__cartas = []

    def receber_carta(self, carta):
        self.__cartas.append(carta)

    def retornar_carta(self, escolha):
        return self.__cartas.pop(escolha)

    def selecionar_acao(self, rodada):
        if len(self.__cartas) == 0:
            print("O jogador não tem cartas para escolher.")
            return False
        else:
            escolha_valida = False
            while not escolha_valida:
                decisao:int = self.__tomar_decisao()
                escolha = self.__validar_escolha(decisao, rodada)
                escolha_valida = escolha != False
        return escolha

    def estampar_equipe(self, equipe):
        self.__nome = f'{self.__nome} ({equipe})'

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