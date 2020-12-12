from random import choice
primeiro = input('Digite o nome do primeiro aluno: ')
segundo = input('Digite o nome do segundo aluno: ')
terceiro = input('Digite o none do terceiro aluno: ')
quarto = input('Digite o nome do quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]

print(f'O aluno sorteado foi {choice(lista)}')
