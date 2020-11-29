# Confere se o número informado é Primo ou não.

num = int(input('Digite um número inteiro: \033[36m'))
cont = 0
for c in range(1, num + 1):
    if(num % c == 0):
        print(f'\033[32m', end = ' ') # cor verde
        cont += 1
    else:
        print(f'\033[31m', end = ' ') # cor vermelha
    print(f'{c}', end = ' ')
print(f'\033[m\nO número {num} foi divisível {cont} vezes.')

if(cont == 2):
    print(f'Portanto, {num} é um número Primo.')
else:
    print(f'Por ser divisível, mais de duas vezes ou menos, o número {num} não é Primo.')
