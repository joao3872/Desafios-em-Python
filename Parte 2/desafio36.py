casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Quanto você ganha? R$ '))
anos = int(input('Em quantos anos você pagará? '))
prestacao = (casa / 12) / anos
confiraE = (salario * (30/100))
print('Para fazer o pagamento de uma casa de R$ {:.2f} em {} anos, a prestação terá um total de R$ {:.2f}'.format(casa, anos, prestacao))

if(prestacao <= confiraE):
    print('Empréstimo Aprovado !')
else:
    print('Empréstimo Negado. Pois, 30% do seu salário é igual a R$ {:.2f} que é menor do que a prestação: R$ {:.2f}'.format(confiraE, prestacao))
