media = 0
homem = 0
idadeH = 0
nomeH = ''
mulher = 0
maior20 = 0
for c in range(1, 5):
    nome = input(f'Informe o nome da {c}º pessoa: ').strip().upper()
    idade = int(input(f'Informe a idade da {c}º pessoa: '))
    sexo = input(f'Informe o sexo da {c}º pessoa com (M / F): ').strip().upper()
    print(' ')
    media += idade / 4
    if(sexo == 'M'):
        homem += 1
        if(idade > idadeH):
            idadeH = idade
            nomeH = nome

    if(sexo == 'F' and idade < 20):
        mulher += 1

    if(sexo == 'F' and idade > 20):
        maior20 += 1

print(f'A média de idade do grupo é: {media} anos')

if(homem != 0):
    print(f'O homem mais velho tem {idadeH} anos e se chama {nomeH}.')
else:
    print('Não existe nenhum Homem neste Grupo.')

if(mulher != 0):
    print(f'Temos {mulher} mulher(es) com menos de 20 anos.')
elif(maior20 != 0):
    print(f'Temos {maior20} mulher(es) com mais de 20 anos.')
else:
    print(f'Não existe nenhuma Mulher neste Grupo. E possui {homem} Homem(ns).')
