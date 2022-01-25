from random import choice
from time import sleep
print('Suas Jogadas: \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA')
jogada = int(input('Qual é a sua Jogada ? '))
jogador = str(jogada).replace('1', 'PEDRA').replace('2', 'PAPEL').replace('3', 'TESOURA')
lista = ['1', '2', '3']
pc = choice(lista).replace('1', 'PEDRA').replace('2', 'PAPEL').replace('3', 'TESOURA')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !')
sleep(1)
resultado = ('Computador jogou {} \nJogador jogou {}'.format(pc, jogador))

if(jogada <= 0 or jogada > 3):
    print('Jogada Inválida. Tente de novo.')
elif(jogador == pc):
    print('{} \nDeu Empate'.format(resultado))
elif(jogador == 'PEDRA' and pc == 'PAPEL'):
    print('{} \nComputador Venceu !'.format(resultado))
elif(jogador == 'PEDRA' and pc == 'TESOURA'):
    print('{} \nJogador Venceu !'.format(resultado))
elif(jogador == 'PAPEL' and pc == 'TESOURA'):
    print('{} \nComputador Venceu !'.format(resultado))
elif(jogador == 'PAPEL' and pc == 'PEDRA'):
    print('{} \nJogador Venceu !'.format(resultado))
elif(jogador == 'TESOURA' and pc == 'PEDRA'):
    print('{} \nComputador Venceu !'.format(resultado))
else:
    print('{} \nJogador Venceu !'.format(resultado))
