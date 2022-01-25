idade = sexo = continua = contH = cont = maior = menor = 0
while True:
    idade = int(input('Digite a idade de uma pessoa: '))
    sexo = input('Digite o sexo (M / F): ').strip().upper()
    continua = input('Deseja continuar ? [Sim / Não]: ').strip().upper()

    if(sexo == 'M'):
        contH += 1
        if idade >= 18:
            maior += 1
    elif(sexo == 'F'):
        cont += 1
        if idade < 20:
            menor += 1
        elif(idade > 20):
            maior += 1
    else:
        print('Sexo Inválido.')

    if(continua == 'SIM'):
        print('---' * 12)
    elif(continua == 'NÃO'):
        break
    else:
        print('Resposta Inválida.')
        break

print(f'\nExiste {maior} pessoa(s) maior(es) de 18 anos no grupo.')
print(f'No grupo, possui {contH} homens. \nE possui, {menor} mulher(es) menor(es) de 20 anos.')
