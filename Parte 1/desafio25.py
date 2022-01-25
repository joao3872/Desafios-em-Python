nome = input('Digite o seu nome completo: ').strip()
s = nome.split()
ss = s[0]
confira = ('Silva'.title() in ss) or ('Silva'.upper() in ss) or ('Silva'.lower() in ss) or ('SILVA' in nome.upper())
z = (ss[0:][5:] in nome)

print('O seu nome possui Silva? {}'.format(confira and z).replace('True', 'Sim').replace('False', 'Não'))
