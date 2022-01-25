from random import sample
valores = tuple(sample(range(11), 5))

print(f'{valores}')
print(f'O maior valor sorteado foi: {max(valores)} \nO menor valor sorteado foi: {min(valores)}')
