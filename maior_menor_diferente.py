# confere qual o menor e o maior número. Conta quantos números foram digitados e exibe a média dos números digitados.

num = media = cont = 0
continua = ''
parar = 'NÃO'
lista = []

while continua != parar:
    num = int(input('Digite um número: '))
    continua = str(input('Deseja continuar ? [Sim / Não] ')).upper()
    cont += 1
    media += num
    lista.append(num)
    if(continua != 'SIM'):
        print(f'\nVocê digitou {cont} número(s) e a Média é {media / cont :.2f}')
        if(cont == 1):
            print('Você digitou apenas um número.')
            exit()
        elif(max(lista) == min(lista)):
            print(f'Os {cont} números são iguais !')
            exit()
        else:
            print(f'O Maior número foi {max(lista)} e o Menor foi {min(lista)}')
            exit()

