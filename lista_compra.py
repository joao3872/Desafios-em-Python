print('-' * 32)
print(f'{"Lista de Compras":^32}')
print('-' * 32)
valores = ('Pão', 1.29, 'Caderno', 20.99, 'Mochila', 159.99, 'Computador', 3000, 'Abacaxi', 7)
for c in range(0, len(valores), 2):
    print(f'{valores[c]:.<20}R$ {valores[c + 1]:>7.2f}')
