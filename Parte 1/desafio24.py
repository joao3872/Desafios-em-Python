cidade = input('Qual é a sua cidade natal? ').strip()
s = cidade.split()
ss = s[0]
confira = ('Santo'.title() in ss) or ('Santo'.upper() in ss) or ('Santo'.lower() in ss) or (cidade[:5].upper() == 'SANTO')

print('Sua cidade possui Santo, no primeiro nome? {}'.format(confira))
