import random
p = input('Digite o nome do Primeiro aluno: ')
s = input('Digite o nome do Segundo aluno: ')
t = input('Digite o nome do Terceiro aluno: ')
q = input('Digite o nome do Quarto aluno: ')
sorteio = (p, s, t, q)

print('O aluno sorteado foi: {}'.format(random.choice(sorteio)))
