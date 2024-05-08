# Declaração de Variáveis
altura = float(0);
ano_nascimento = int(0);
idade = int(0);
nome = str('');
tem_cnh = bool(False);

# Entrada de Dados
nome = input('Digite o seu nome: ');
ano_nascimento = int(input('Digite seu ano de nascimento: '));

if ( ano_nascimento < 1900 or ano_nascimento > 2020 ):
    print('\nDigite um ano de nascimento entre 1900 e 2020');
    exit();

tem_cnh = bool(input('Você tem CNH? (Apertar ENTER se não tiver): '));

# Processamento

idade = 2024 - ano_nascimento;

# Saída de Dados

print(f'Olá, {nome}');
print(f'Você nasceu no ano {ano_nascimento}');
print(f'Você tem {idade} anos');

if ( tem_cnh == True ):
    print('O usuário tem CNH, portanto pode dirigir.');
else:
    print('O usuário NÃO tem CNH, você não deve dirigir.');