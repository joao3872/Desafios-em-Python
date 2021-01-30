from moedas_2 import metadeP, dobroP, porcento10, desconto, moeda

preco = float(input('Digite o preço R$ '))

print(f'A metade de R$ {moeda(preco)} é: R$ {moeda(metadeP(preco))}')
print(f'O dobro de R$ {moeda(preco)} é: R$ {moeda(dobroP(preco))}')
print(f'Com um aumento de 10%, os R$ {moeda(preco)} passa a ser: R$ {moeda(porcento10(preco))}')
print(f'Com um desconto de 10%, os R$ {moeda(preco)} passa a ser: R$ {moeda(desconto(preco))}')
