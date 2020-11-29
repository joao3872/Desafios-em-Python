# Mostra o seu primeiro nome e o último nome.


nome = input('Informe o seu nome completo: ').strip()
nome.upper() and nome.lower()
lista = nome.split()
primeiro = lista[0]
ultimo = lista[-1]

print(f'Seu primeiro nome é: {primeiro} \nE seu último nome é: {ultimo}')
