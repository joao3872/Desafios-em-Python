def resposta():
    while True:
        print('\033[1;31;42m')
        print(f'{"Sistema de Ajuda Python":^51}')
        print('\033[m')
        duvida = str(input('Função ou Dicionário >>> '))

        if duvida.lower() == 'fim':
            print(f'\033[41m{"Fim do Programa.":^51}\033[m')
            break
        else:
            print(f'\033[34;43mGerando o Manual para: {duvida}')
            print('\033[m')
            print(f'\033[30;107m')
            help(duvida)
            print('\033[m')

# Programa principal
resposta()
