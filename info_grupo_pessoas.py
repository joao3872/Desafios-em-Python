pessoa = list()
grupo = dict()
soma = media = cont = 0
while True:
    grupo['Nome'] = str(input('Nome: '))
    grupo['Sexo'] = str(input('Informe o sexo [M / F] ')).strip().upper()

    while grupo['Sexo'] not in 'MF':
        print('Valor Inválido. Digite M ou F')
        grupo['Sexo'] = str(input('Informe o sexo [M / F] ')).strip().upper()
    grupo['Idade'] = int(input('Qual a sua idade ? '))
    cont += 1
    soma += grupo['Idade']
    media = soma / cont
    pessoa.append(grupo.copy())
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar ? [S / N] ')).strip().upper()
        if continua != 'S' and continua != 'N':
            print('Valor Inválido. Digite S ou N')
    if continua == 'N':
        break

print(f'\nTemos {len(pessoa)} pessoas no Grupo.')
print(f'A média de idade é {media :.2f} anos.')

if(grupo['Sexo'] == 'F'):
    print(f'As Mulheres cadastradas:', end = ' ')
    for c, v in enumerate(pessoa):
        if pessoa[c]['Sexo'] == 'F':
            print(f'{pessoa[c]["Nome"]}', end = ' ')
else:
    print('O grupo não possui Mulheres.')

print('\nLista com as pessoas, que estão acima da média:')
for c in pessoa:
    if(c['Idade'] > media):
        print(f' -> Nome: {c["Nome"]}; Sexo: {c["Sexo"]}; Idade: {c["Idade"]};')
