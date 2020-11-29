# Jogo da Adivinhação de 0 a 10.

from random import randint
from time import sleep
print('Olá te desafio a Adivinhar, o que pensei.')
print('Pensei em um número entre 0 e 10. \nVocê consegue adivinhar o número que pensei ?')
palpite = int(input('Qual é o seu palpite ? \033[36m'))
tentativas = 1
computador = randint(0, 10)
sleep(1)
while palpite != computador:
    tentativas += 1
    
    if(computador > palpite):
        palpite = int(input('\033[33m Maior... Tente mais uma vez: \033[36m'))
    else:
        palpite = int(input('\033[31m Menor... Tente mais uma vez: \033[36m'))
    print('\033[m Analisando...'), sleep(2)

if(palpite == computador):
    print(f'\033[32m Acertou com {tentativas} tentativa(s). Meus Parabéns !\033[m')
