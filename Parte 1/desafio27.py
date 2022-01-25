nome = input('Digite o seu nome completo: ').strip()
nome.upper() and nome.lower()
p = nome.split()
pp = p[0]
ultimo = p[-1]

print('Seu primeiro nome é: {} \nE seu último nome é: {}'.format(pp, ultimo))
