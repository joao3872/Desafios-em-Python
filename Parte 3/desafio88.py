from random import sample
from time import sleep
print('-' * 35)
print(f'{"Aposta para a Mega-Sena":^35}')
print('-' * 35)

lista = []
apostas = int(input('Quantas apostas deseja fazer ? '))
print(f"{'<' * 8} Sorteando {apostas} Jogos {'>' * 8}")

for cont in range(apostas):
    lista.append(sorted(sample(range(1, 61), 6)))
    print(f'\n Jogo {cont + 1}: {lista}')
    lista.clear()
    sleep(1)
