# confirma se um número inteiro, é par ou ímpar.

num = int(input('Digite um número inteiro: '))
par = (num % 2)

if(par == 0):
    print(f'O número: {num} é Par')
else:
    print(f'O número: {num} é Ímpar')
