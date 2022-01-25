from math import sqrt, pow
op = float(input('Informe o comprimento do cateto oposto: '))
adj = float(input('Informe o comprimento do cateto adjacente: '))
hip = sqrt(pow(op, 2) + pow(adj, 2)) #pow é a potência, ex.: 5 * 5

print('A hipotenusa é igual a {:.2f}'.format(hip))
