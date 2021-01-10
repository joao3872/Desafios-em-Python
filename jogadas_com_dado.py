from random import randint
from time import sleep
from operator import itemgetter
resultado = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}
ranking = dict()
print('Jogadas com o Dado')
for jogador, valor in resultado.items():
    print(f'{jogador} tirou {valor} no Dado')
    sleep(0.7)

ranking = sorted(resultado.items(), key = itemgetter(1), reverse = True)
print('<>' * 18)
print('Ranking dos Jogadores:')
for cont, jogo in enumerate(ranking):
    print(f'{cont + 1}º lugar: {jogo[0]} com {jogo[1]}')
    sleep(0.7)
