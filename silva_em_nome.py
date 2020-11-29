# conferi se tem Silva no nome.

nome = input('Digite seu nome completo: ')
lista = nome.split()
ver = lista[0]
confira = ('Silva.title() in ver) or ('Silva'.lower() in ver) or ('SILVA' in nome.upper())
tudo = (ver[0:][5:] in nome)

print(f'Seu nome possui Silva ? {confira and tudo}'.replace('True', 'Sim').replace('False', 'Não'))
