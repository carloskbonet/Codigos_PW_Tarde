
# Variáveis
ano = int(0);
resultado = int(0);
anterior = int(0);
proximo = int(0);

print('O algoritmo verificará se o ano digitado é bissexto ou não.');

# Inputs

ano = int(input('Digite: '));

if ( ano < 0 or ano > 2050 ):
    print('Ano inválido, digite algo entre 0 e 2050');
    exit();

# Processamento

resultado = ano % 4;

# Saída de Dados
print('\n');

if ( resultado == 0 ):
    print(f'O ano {ano} é um ano bissexto.');
else:
    print(f'O ano {ano} NÃO é bissexto.');
    anterior = ano - resultado;
    proximo = anterior + 4;
    print(f'Último ano bissexto: {anterior}');
    print(f'O próximo bissexto será: {proximo}');

# Extra: Qual foi o último ano bissexto? quando será o próximo?