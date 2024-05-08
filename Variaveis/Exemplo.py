# Declaração de Variáveis
altura = float(0);
ano_nascimento = int(0);
idade = int(0);
nome = str('');
tem_cnh = bool(False);

# Entrada de Dados
nome = input('Digite o seu nome: ');
ano_nascimento = int(input('Digite seu ano de nascimento: '));
tem_cnh = bool(input('Você tem CNH? (Apertar ENTER se não tiver): '));

# Processamento
idade = 2024 - ano_nascimento;

# Saída de Dados

print(f'Olá, {nome}');
print(f'Você nasceu no ano {ano_nascimento}');
print(f'Você tem {idade} anos');
print(f'Possui CNH? {tem_cnh}');