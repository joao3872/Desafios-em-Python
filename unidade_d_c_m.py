# Exibe a Unidade, Dezena, Centena é Milhar de um número inteiro. 

num = int(input('Digite um número inteiro: '))
valor = num.zfill(4)
print(f'O número {num} possui:')
print(f'Unidade: {valor[3]} \nDezena: {valor[2]} \nCentena: {valor[1]} \nMilhar: {valor[0]}')

