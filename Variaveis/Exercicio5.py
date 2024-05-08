nome = str('');
sobrenome = str('');
nomeCompleto = str('');

print('Digite seus dados. O algoritmo exibirá seu nome completo.');

nome = input('Nome: ');
sobrenome = input('Sobrenome: ');

nomeCompleto = nome + ' ' + sobrenome;

print(f'Olá, {nomeCompleto}');