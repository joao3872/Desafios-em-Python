# O clássico jogo da velha.

from random import choice
from time import sleep
print('Escolha uma jogada: \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA')
jogada = int(input('Qual é a sua jogada ? '))
jogador = str(jogada).replace('1', 'PEDRA').replace('2', 'PAPEL').replace('3', 'TESOURA')
lista = ['1', '2', '3']
pc = choice(lista).replace('1', 'PEDRA').replace('2', 'PAPEL').replace('3', 'TESOURA')
resultado = (f'Computador jogou {pc} \n Jogador jogou {jogador}')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !')
sleep(1)

if(jogada <= 0 or jogada > 3):
    print('Jogada Inválida. Tente novamente.')
elif(jogador == pc):
    print(f'{resultado} \nDeu Empate')
elif(jogador == 'PEDRA' and pc == 'PAPEL'):
    print(f'{resultado} \nComputador Venceu !')
elif(jogador == 'PEDRA' and pc == 'TESOURA'):
    print(f'{resultado} \nJogador Venceu !')
elif(jogador == 'PAPEL' and pc == 'TESOURA'):
    print(f'{resultado} \nComputador Venceu !')
elif(jogador == 'PAPEL' and pc == 'PEDRA'):
    print(f'{resultado} \nJogador Venceu !')
elif(jogador == 'TESOURA' and pc == 'PEDRA'):
    print(f'{resultado} \nComputador Venceu !')
else:
    print(f'{resultado} \nJogador Venceu !')

