class Carta:
    def __init__(self, posicao, naipe):
        self.__posicao = posicao
        self.__naipe = naipe
        self.__nome = f'{posicao.name} de {naipe.name}'

    @property
    def nome(self):
        return self.__nome

    @property
    def posicao(self):
        return self.__posicao

    @property
    def naipe(self):
        return self.__naipe