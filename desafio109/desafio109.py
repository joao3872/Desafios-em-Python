from moedas_3 import metadeP, dobroP, porcento10, desconto, moeda

preco = float(input('Digite o preço R$ '))
formatacao = str(input('Deseja adicionar formatação, ao preço? Digite S para sim ou N para não: ')).strip().upper()

if formatacao == 'S':
    print(f'A metade de {moeda(preco)} é: {moeda(metadeP(preco))}')
    print(f'O dobro de {moeda(preco)} é: {moeda(dobroP(preco))}')
    print(f'Com um aumento de 10%, os {moeda(preco)} passa a ser: {moeda(porcento10(preco))}')
    print(f'Com um desconto de 10%, os {moeda(preco)} passa a ser: {moeda(desconto(preco))}')
else:
    print(f'A metade de {preco} é: {metadeP(preco)}')
    print(f'O dobro de {preco} é: {dobroP(preco)}')
    print(f'Com um aumento de 10%, os {preco} passa a ser: {porcento10(preco)}')
    print(f'Com um desconto de 10%, os {preco} passa a ser: {desconto(preco)}')
