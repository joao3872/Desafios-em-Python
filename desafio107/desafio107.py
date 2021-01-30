from moedas import metadeP, dobroP, porcento10, desconto

preco = float(input('Digite o preço R$ '))

print(f'A metade de R$ {preco :.2f} é: R$ {metadeP(preco) :.2f}')
print(f'O dobro de R$ {preco :.2f} é: R$ {dobroP(preco) :.2f}')
print(f'Com um aumento de 10%, os R$ {preco :.2f} passa a ser: R$ {porcento10(preco) :.2f}')
print(f'Com um desconto de 10%, os R$ {preco :.2f} passa a ser: R$ {desconto(preco) :.2f}')
