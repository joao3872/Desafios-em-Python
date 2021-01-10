nome = str(input('Nome: '))
media = float(input('Média de 0 a 10: '))
valores = {'Nome': nome, 'Média': media}

print(f'\n-> O Nome do Aluno é: {valores["Nome"]}')
print(f'-> A Média do Aluno é: {valores["Média"] :.1f}')

if(valores['Média'] >= 7):
    valores['Situação'] = '-> Parabéns ! Você foi Aprovado !'
    print(f'{valores["Situação"]}')
elif(valores['Média'] >= 5):
    valores['Situação'] = '-> Você está de Recuperação. Se esforce mais !'
    print(f'{valores["Situação"]}')
else:
    valores['Situação'] = '-> Você está Reprovado.'
    print(f'{valores["Situação"]}')
