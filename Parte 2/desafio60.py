num = int(input('Digite um número, para conferir o seu Fatorial: '))
fatorial = num
multiplica = 1
print(f'{num}! =', end = ' ')
while fatorial != 0:
    print(f'{fatorial}', end = ' ')
    if(num == 1):
        print(' ')
    elif(fatorial > 1):
        print('X', end = ' ')
    else:
        print('=', end = ' ')
    multiplica *= fatorial
    fatorial -= 1
if num == 1:
    print(' ')
else:
    print(f'{multiplica}')
