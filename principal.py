from baralho import Baralho 
from carta import Carta
from jogador import Jogador 

print ("Bem-vindo ao Cassino Relâmpago!")
print ('Você pode escolher essas opções: \n1- Jogar \n2- Tutorial')
acao = int(input("Digite sua escolha: "))
if acao == 1:
    print('Bem-vindo ao 21')
    n = input("Digite o nome do jogador 1: ")
    jogador1 = Jogador(n)

    n2 = input("Digite o nome do jogador 2: ")
    jogador2 = Jogador(n2)

    jogador1.receber_cartas()
    print('O jogador {} recebeu as cartas'.format(n))
    jogador2.receber_cartas()
    print('O jogador {} recebeu as cartas'.format(n2))
    jogador1.mostrar_mao()
    jogador2.mostrar_mao()



elif acao == 2:
    print ("O estilo do jogo é '21' onde duas pessoas vão receber 2 cartas, a pessoa que chegar mais perto de 21, ganha.")
    print ("Caso o valor que o jogador receber ficar longe de 21, o mesmo pode pedir mais uma carta, se passar de 21 perde.")
    print ("Caso o jogador fique com um valor valor aproximado de 21, exemplo o 18, o jogador não é obrigado a pedir mais carta.")
    print ("Os valores são 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete, Dama, Rei e Ás")
    print ("Valete, Dama, Rei continuam valendo 10 e Ás é 1")
    print ("Dependendo da combinação de cartas que receber, você fica com 21, exemplo Rei e Ás")    
    print ("Ganha quem chegar mais perto de 21!\n")

    print ('Você pode escolher essas opções: \n1- Jogar \n2- Tutorial')
    acao = int(input("Digite sua escolha: "))



