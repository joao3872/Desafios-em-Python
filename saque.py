# Mostra a quantidade de cédulas, de acordo com o valor á ser sacado.

saque = nota100 = 0
while saque == 0:
    saque = int(input('Que Valor você quer Sacar ? R$ '))
    if(saque < 100):
        print('Neste caso, a cédula de R$ 100,00 não pode ser usada.')
    else:
        nota100 = saque // 100
        saque %= 100
        print(f'{nota100} cédula(s) de R$ 100')

    if(saque < 50):
        print('Neste caso, a cédula de R$ 50,00 não pode ser usada.')
    else:
        nota50 = saque // 50
        saque %= 50
        print(f'{nota50} cédula(s) de R$ 50')  
    
    if(saque < 20):
        print('Neste caso, a cédula de R$ 20,00 não pode ser usada.')
    else:
        nota20 = saque // 20
        saque %= 20
        print(f'{nota20} cédula(s) de R$ 20')
    
    if(saque < 10):
        print('Neste caso, a cédula de R$ 10,00 não pode ser usada.')
    else:
        nota10 = saque // 10
        saque %= 10
        print(f'{nota10} cédula(s) de R$ 10')
        
    if(saque < 5):
        print('Neste caso,a cédula de R$ 5,00 não pode ser usada.')
    else:
        nota5 = saque // 5
        saque %= 5
        print(f'{nota5} cédula(s) de R$ 5')

    if(saque >= 2):
        nota2 = saque // 2
        saque %= 2
        print(f'{nota2} cédula(s) de R$ 2')
    else:
        print('Neste caso, a cédula de R$ 2,00 não pode ser usada.')
    
    if(saque <= 0):
        print('Embora, as cédulas de R$ 1,00 não exista mais, serve para ser usada neste programa.')
        break
    else:
        nota1 = saque // 1
        print(f'{nota1} cédula(s) de R$ 1')
        break
