from random import randint
print('Jogo do Par ou Ímpar \n')
num = escolha = cont = 0
while True:
    num = int(input('Digite um número: '))
    escolha = str(input('Escolha Par ou Ímpar: ')).strip().upper()
    computador = randint(0, num)
    soma = num + computador
    print(f'Você escolheu {num} e o computador {computador}. Total de {soma} deu', end = ' ')
    print('Par' if soma % 2 == 0 else 'Ímpar')
    if(escolha == 'PAR'):
        if(soma % 2 == 0):
            print('Você venceu !')
            cont += 1
        else:
            print('Você perdeu.')
            break
            
    elif(escolha == 'ÍMPAR'):
        if(soma % 2 == 1):
            print('Você venceu !')
            cont += 1
        else:
            print('Você perdeu.')
            break
    print('Jogando novamente...')         
