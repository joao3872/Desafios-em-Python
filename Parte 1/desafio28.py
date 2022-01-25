from random import choice
from time import sleep
print('<-' * 28)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('->' * 28)
num = int(input('Qual foi o número que pensei? '))
escolha = [0, 1, 2, 3, 4, 5]
r = choice(escolha)
print('PROCESSANDO...')
sleep(2)

if(num != r):
    print('Ganhei! Eu pensei no número {} e não no {}'.format(r, num))
else:
    print('Muito bem! Você conseguiu ganhar de mim!')
