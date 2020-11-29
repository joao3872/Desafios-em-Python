# jogo de adivinhação...

from random import choice
from time import sleep
print('<--' * 17)
print('Vou pensar em um número de 0 a 5. Tente me derrotar!')
print('-->' * 17)
num = int(input('Digite um número: '))
ordem = [0, 1, 2, 3, 4, 5]
escolha = choice(ordem)
print('PROCESSANDO...')
sleep(2)

if(num != escolha):
    print('Ganhei! Eu pensei no número {escolha} e não no {num}.')
else:
    print('Muito bem você ganhou de mim!')
