sal = float(input('Digite seu salário: '))
poc = sal * 15/100
aum = sal + poc

print('Seu antigo salário era de R$ {}, com 15% de aumento, seu salário passou a ser R$ {:.2f}'.format(sal, aum))
