num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
tupla = (num1, num2, num3, num4)
cont = 0

print(f'O número 9 apareceu {tupla.count(9)} vez(es).')

if(3 in tupla):
    print(f'O número 3 apareceu na {tupla.index(3) + 1}° posição.')
else:
    print('O número 3 não apareceu, nenhuma vez na tupla.')

print('O(s) número(s) Par(es) digitado(s) é:', end = ' ')

for pares in tupla:   
    if(pares % 2 == 0):
        print(f'{pares}', end = ' ')
        cont += 1   

if(cont == 0):
    print('A tupla não possui nenhum número Par.')
