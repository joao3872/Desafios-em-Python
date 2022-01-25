def area(largura, comprimento):
    area = largura * comprimento
    print(f'\nA área de um terreno {largura :.1f} X {comprimento :.1f} é de {area} m²')

area(largura = float(input('Largura (m): ')), comprimento = float(input('Comprimento (m): ')))
