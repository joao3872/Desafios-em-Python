from time import sleep
num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print('\nVocê tem essas opções: \n[1] Somar \n[2] Multiplicar \n[3] Maior Valor \n[4] Novos Números \n[5] Sair do Programa')
    opcao = int(input('Qual a sua opção ? '))
    if(opcao == 1):
        print(f'A Soma de {num} + {num2} é {num + num2}')
    elif(opcao == 2):
        print(f'A Multiplicação de {num} X {num2} é {num * num2}')
    elif(opcao == 3):
        if(num > num2):
            print(f'O maior número entre {num} e {num2} é {num}')
        else:
            print(f'O maior número entre {num} e {num2} é {num2}')
    elif(opcao == 4):
        print('Informe os números novamente.')
        num = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif(opcao != 5):
        print('Valor inválido. Tente novamente.')
    else:
        print(''), sleep(2)
        print('<>' * 12)
        print('Programa finalizado.')
