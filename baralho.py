from carta import Carta
import random

class Baralho:
    def _init_(self):
        self.cartas = []
        self._criar_baralho()

    def _criar_baralho(self):
        naipes = ['Espadas', 'Paus', 'Copas', 'Ouros']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']
        for naipe in naipes:
            for valor in valores:
                self.cartas.append(Carta(valor, naipe))

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_cartas(self, num_cartas):
        return [self.cartas.pop() for _ in range(num_cartas)]