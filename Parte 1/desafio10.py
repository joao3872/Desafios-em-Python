real = float(input('Digite um valor em Reais, e descubra quantos Dólares você pode comprar: '))
dol = (real * 0.18)

print('Com R$ {}, você pode comprar US$ {:.2f}'.format(real, dol))
