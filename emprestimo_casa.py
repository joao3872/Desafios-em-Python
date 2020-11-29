# conferi, se é possível uma pessoa pagar uma casa, de acordo com o seu salário, e a aprovação do empréstimo.

casa = float(input('Informe o valor da casa: '))
salario = float(input('Digite o salário: '))
ano = int(input('Em quantos anos, você quer pagar? '))
prestacao = (casa / 12) / ano
confiraE = (salario * (30/100))
print(f'Para fazer o pagamento de uma casa de R$ {casa :.2f} em {ano} anos, a prestação terá um total de R$ {prestacao :.2f}')

if(prestacao <= confiraE):
    print('Empréstimo Aprovado !')
else:
    print(f'Empréstimo Negado. Pois, 30% do seu salário é igual a R$ {confiraE :.2f} que é menor do que a prestação: R$ {prestacao :.2f}')

