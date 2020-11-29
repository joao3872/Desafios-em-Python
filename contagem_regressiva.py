# contagem de 10 até 0, com For e com um intervalo de 1 segundo, de um para o outro.

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Feliz Ano Novo !!!')

