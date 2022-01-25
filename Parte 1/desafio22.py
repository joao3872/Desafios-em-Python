nome = input('Informe o seu nome completo: ').strip()
nomeM = nome.upper()
nomem = nome.lower()
semE = nome.replace(' ', '')
todas = len(semE)
primeiroN = nome.split()
pNome = len(primeiroN[0])

print('Seu nome com letras maiúsculas: {} \nSeu nome com letras minúsculas: {} \nTotal de letras de seu nome: {} \nQuantidade de letras de seu primeiro nome: {}'.format(nomeM, nomem, todas, pNome))
