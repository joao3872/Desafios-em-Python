futebol = dict()
gol = []
futebol['Jogador'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas Partidas {futebol["Jogador"]} jogou ? '))

if(partidas == 0):
    print(f'\n{futebol["Jogador"]} não jogou nenhuma Partida. \nPortanto, não tem Gols, para ser registrado.')
else:
    for cont in range(0, partidas):
        gol.append(int(input(f'Quantos Gols foram feitos na partida {cont + 1} ? ')))
        futebol['Gols'] = gol
        futebol['Total'] = sum(gol)
    print(f'\n {futebol}')

    print('<>' * 25)
    print(f'O nome do Jogador é: {futebol["Jogador"]}')
    print(f'Os gols do jogador por partida: {futebol["Gols"]}')
    print(f'Total de Gols feitos: {futebol["Total"]}')
    print('<>' * 25)

    print(f'O Jogador {futebol["Jogador"]} jogou {partidas} Partidas')
    for c, p in enumerate(futebol['Gols']):
        print(f' -> Na partida {c + 1}, fez {p} Gols')
    print(f'Durante as {partidas} partidas o Jogador, fez um Total de {futebol["Total"]} Gols')
