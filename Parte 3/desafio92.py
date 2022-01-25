from datetime import date
atual = date.today().year

informacoes = dict()
informacoes['Nome'] = str(input('Digite o seu Nome: '))
nascimento = int(input('Digite o seu ano de nascimento: '))
informacoes['Carteira'] = int(input('Carteira de Trabalho (0 não tem) '))
informacoes['Idade'] = atual - nascimento

if(informacoes['Carteira'] != 0):
    informacoes['Contratação'] = int(input('Ano de Contratação: '))
    informacoes['Salário'] = float(input('Seu Salário: '))
    informacoes['Aposentar'] = ((informacoes['Contratação'] + 35) - atual) + informacoes['Idade']

for k, v in informacoes.items():
    print(f'{k} tem o valor {v}')
