# Classificação dos Times de Futebol em 2019...

classificacao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
primeiros = classificacao[0:5]
ultimos = classificacao[-4:]
alfabetica = sorted(classificacao)
posicaoC = classificacao.index('Chapecoense') + 1

print(f'Os 5 primeiros são: {primeiros} \n')
print(f'Os 4 últimos são: {ultimos} \n')
print(f'Times em Ordem Alfabética: {alfabetica} \n')
print(f'O Chapecoense está na {posicaoC}° posição.')
