def ficha(nome, gols):
    if nome == '':
        nome = f'\033[33m {"<Desconhecido>"} \033[m'
    if gols == '':
        gols = f'\033[33m {"0"} \033[m'
    return f'O Jogador: {nome}, fez {gols} gol(s) no campeonato.'

nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
print(ficha(nome, gols))
