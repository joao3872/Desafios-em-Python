def linha(msg):
    print('-' * 50)
    print(f'{msg}')
    print('-' * 50)

def inteiro(num):
    while True:
        try:
            valor = int(input(num))
        except (TypeError, ValueError):
            print('Erro, tente de novo.')
        except (KeyboardInterrupt):
            print('Usuário não quis digitar.')
            return 0
        else:
            return valor

def menu():
    from manipulaArquivo import existeA, criaA, lerA, cadastrar
    from time import sleep
    arq = 'pessoas.txt'

    if not existeA(arq):
        criaA(arq)
    
    while True:
        linha(f'{"Menu Principal":>32}')
        print('1 - Ver Pessoas Cadastradas')
        print('2 - Cadastrar Nova Pessoa')
        print('3 - Sair Do Sistema')
        print('-' * 50)

        opcao = inteiro('Digite a sua opção: ')
        if opcao <= 0 or opcao > 3:
            print('Erro.')
        elif opcao == 1:
            linha(f'{"Ver Pessoas Cadastradas":>37}')
            lerA(arq)
        elif opcao == 2:
            linha(f'{"Cadastrar Nova Pessoa":>37}')
            nome = str(input('Digite um Nome: '))
            idade = inteiro('Digite a Idade: ')
            cadastrar(arq, nome, idade)
        else:
            print('\nSaindo do Programa...')
            sleep(1)
            print('\nVolte Sempre !')
            exit()
