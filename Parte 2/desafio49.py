valor = int(input('Digite um número, para mostrar a Tabuada: '))
valor2 = int(input('Até onde você, deseja multiplicar? '))

for c in range(1, valor2 + 1):
    print(f'{valor} X {c :2} = {valor * c}')
