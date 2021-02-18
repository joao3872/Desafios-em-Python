def existeA(arq):
    try:
        arquivo = open(arq, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaA(arq):
    try:
        arquivo = open(arq, 'wt+')
        arquivo.close()
    except:
        print('Erro na Criação do Arquivo.')
    else:
        print(f'Arquivo: {arq} Criado com Sucesso !')

def lerA(arq):
    try:
        arquivo = open(arq, 'rt')
    except:
        print('Erro de Leitura do Arquivo.')
    else:
        for linha in arquivo:
            dado = linha.split(':')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')
    finally:
        arquivo.close()

def cadastrar(arq, nome='Sem Nome', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Erro na Abertura do Arquivo.')
    else:
        try:
            arquivo.write(f'{nome}:{idade}\n')
        except:
            print('Erro no Cadastro de Nome e Idade.')
        else:
            print(f'{nome} Cadastrado(a) com Sucesso !')
            arquivo.close()
