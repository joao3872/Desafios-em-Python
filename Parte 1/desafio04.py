d = input('Digite alguma coisa: ')

print('O tipo primitivo deste valor:', type(d))
print('Só tem espaços?', d.isspace())
print('É um número?', d.isnumeric()) #conferi se é número
print('É alfabético?', d.isalpha()) #conferi se é alfabético
print('É alfanumérico?', d.isalnum()) #conferi se é alfanumérico
print('Está em maiúsculas?', d.isupper()) #conferi se o texto é maiúsculo
print('Está em minúsculas?', d.islower()) #conferi se o texto é minúsculo
print('Está capitalizada?', d.istitle()) #conferi se está capitalizado
