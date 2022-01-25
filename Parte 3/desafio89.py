lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    continua = str(input('Deseja continuar? [Sim / Não] ')).strip().upper()
    if(continua == 'SIM'):
        print()
    elif(continua == 'NÃO'):
        break
    else:
        print('Valor Inválido. Tente de novo...')
print('<>' * 20)

print(f'{"Nº"} {"Nome":>10} {"Média":>9}')
print('-' * 25)
for num, aluno in enumerate(lista):
    print(f'{num} {aluno[0]:>10} {aluno[2]:>9.1f}')
print('-' * 30)

while True:
    mostra = int(input('Você quer ver a nota, de qual aluno(a)? (999 para finalizar.) '))
    if(mostra == 999):
        print('Programa finalizado.')
        break
    if(mostra <= len(lista) - 1):
        print(f'As notas de {lista[mostra][0]} são {lista[mostra][1]}')
