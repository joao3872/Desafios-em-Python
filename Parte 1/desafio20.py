from random import shuffle
p = input('Nome do primeiro aluno: ')
s = input('Nome do segundo aluno: ')
t = input('Nome do terceiro aluno: ')
q = input('Nome do quarto aluno: ')
lista = [p, s, t, q]
shuffle(lista)

print('A ordem de apresentação do alunos é: {}'.format(lista))
