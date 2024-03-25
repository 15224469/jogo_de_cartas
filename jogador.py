from baralho import Baralho

class Jogador:
    def __init__(self,nome):
        self.nome = nome 
        self.mao = []

    def receber_cartas(self):
        self.mao.append(Baralho.distribuir_cartas(2))

    def mostrar_mao(self):
        print ('{self.nome} tem as seguintas cartas na mão: ')
        for carta in self.mao:
            print (carta)