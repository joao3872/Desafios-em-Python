def escreva(mensagem):
    tamanho = len(mensagem) + 6
    print(f'{"~"}' * tamanho)
    print(f'   {mensagem}')
    print(f'{"~"}' * tamanho)

escreva('Curso de Python !')
escreva('Desejamos um ano melhor !')
escreva('O Mundo !')
