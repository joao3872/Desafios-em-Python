# Mostra a PA do número e pode adicionar quantos termos a mais, você quiser

print('Super Gerador de PA \n')
termo = int(input('Digite o Termo: '))
razao = int(input('Digite a Razão: '))
calculo = 1
novo = 0
adicione = 10

while adicione != 0:
    novo += adicione
    while calculo <= novo:
        decimo = termo + (calculo - 1) * razao
        print(f'{decimo}', end = ' -> ')
        calculo += 1
    print('Pausa')
    adicione = int(input('\nQuantos termos, você deseja mostrar a mais ? \nDigite 0 para finalizar o programa. '))

print(f'\nPrograma finalizado. Com {novo} termos mostrados.')


