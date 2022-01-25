futebol = dict()
gol = []
tempo = list()
while True:
    futebol.clear()
    futebol['Jogador'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas Partidas {futebol["Jogador"]} jogou ? '))
    gol.clear()
    
    for cont in range(0, partidas):
        gol.append(int(input(f'Quantos Gols foram feitos na partida {cont + 1} ? ')))
    futebol['Gols'] = gol[:]
    futebol['Total'] = sum(gol)
    tempo.append(futebol.copy())
    
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar ? [S / N] ')).strip().upper()
        if(continua != 'S' and continua != 'N'):
            print('Valor Inválido. Digite S ou N')
    if continua == 'N':
        break

print('<>' * 25)
print('cod ', end = ' ')
for i in futebol.keys():
    print(f'{i:<15}', end = ' ')
print()
print('-' * 48)

for c, v in enumerate(tempo):
    print(f'{c:>3}', end = ' ')
    for d in v.values():
        print(f'{str(d):<15}', end = ' ')
    print()
print('-' * 48)

while True:
    mostra = int(input('Dados de qual Jogador ? (999 para parar)'))
    if mostra == 999:
        break
    elif mostra >= len(tempo):
        print(f'Não existe Jogador com este código: {mostra}')
    else:
        print(f' - Levantamento do Jogador: {tempo[mostra]["Jogador"]}')
        for c, p in enumerate(tempo[mostra]['Gols']):
            print(f' -> Na partida {c + 1}, fez {p} Gols')
print('Fim do Programa.')
