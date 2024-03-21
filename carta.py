class Carta:
    def _init_(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        
    def _str_(self):
        return '{self.valor} de {self.naipe}'