num = int(input('Digite um número inteiro: '))
veja = num % 2

if(veja == 0):
    print('O número {} é Par'.format(num))
else:
    print('O número {} é Ímpar'.format(num))
