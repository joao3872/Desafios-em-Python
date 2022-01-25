lar = float(input('Informe a largura da parede em metros: '))
alt = float(input('Informe a altura da parede em metros: '))
area = (lar * alt)
tin = (area / 2)

print('A área da parede é {}m² e a quantidade de tinta para pintar a parede é de {:.1f}L'.format(area, tin))
