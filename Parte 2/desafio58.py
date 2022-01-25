from random import randint
from time import sleep
print('Olá te desafio a Adivinhar, o que pensei.')
print('Pensei em um número entre 0 e 10. \nVocê consegue adivinhar o número que pensei ?')
palpite = int(input('Qual é o seu palpite ? '))
tentativas = 1
computador = randint(0, 10)
sleep(1)
while palpite != computador:
    tentativas += 1

    if(computador > palpite):
        palpite = int(input('Maior... Tente mais uma vez: '))
    else:
        palpite = int(input('Menor... Tente mais uma vez: '))
    print('Analisando...'), sleep(2)

if(palpite == computador):
    print(f'Acertou com {tentativas} tentativa(s). Meus Parabéns !')
