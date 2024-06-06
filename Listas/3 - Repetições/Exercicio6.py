# Variáveis de input
altura_1 = float(0);
altura_2 = float(0);
crescimento_1 = float(0);
crescimento_2 = float(0);

# Variáveis do processamento
menor_inicialmente = float(0);
maior_inicialmente = float(0);

menor_crescimento = float(0);
maior_crescimento = float(0);

taxa_crescimento_menor = float(0);
taxa_crescimento_maior = float(0);

# Variáveis da repetição
count = int(1);
limit = int(20);


# Explicação
print('O algoritmo acompanha o crescimento anual de 2 pessoas. Preencha os valores');


# Input
altura_1 = float(input('Digite a altura da primeira pessoa: '));
altura_2 = float(input('Digite a altura da segunda pessoa: '));

crescimento_1 = float(input('Crescimento da pessoa 1 (Em centímetros) : '));
crescimento_2 = float(input('Crescimento da pessoa 2 (Em centímetros) : '));


# Processamento

crescimento_1 = crescimento_1 / 100;
crescimento_2 = crescimento_2 / 100;


if ( altura_1 < altura_2 ):
    # O menor é a pessoa 1
    menor_inicialmente = altura_1;
    maior_inicialmente = altura_2;
    # Atribuir a taxa de crescimento para as variáveis com nomes "menor" e "maior"
    taxa_crescimento_menor = crescimento_1;
    taxa_crescimento_maior = crescimento_2;
else:
    # O menor é a pessoa 2
    menor_inicialmente = altura_2;
    maior_inicialmente = altura_1;
    # Atribuir a taxa de crescimento para as variáveis com nomes "menor" e "maior"
    taxa_crescimento_menor = crescimento_2;
    taxa_crescimento_maior = crescimento_1;


menor_crescimento = menor_inicialmente;
maior_crescimento = maior_inicialmente;

while ( count <= limit ):
    print(f'\nAno {count}.');

    menor_crescimento = round( menor_crescimento + taxa_crescimento_menor , 2);
    maior_crescimento = round( maior_crescimento + taxa_crescimento_maior , 2);

    if ( menor_crescimento > 2.2 or maior_crescimento > 2.2 ):
        print('Altura limite alcançada.');
        print('A partir desse ano, ambos não crescerão');
        exit();

    print(f'Menor: {menor_crescimento}\nMaior: {maior_crescimento}');

    if ( menor_crescimento > maior_crescimento ):
        print(f'A pessoa que inicialmente tinha {menor_inicialmente}m');
        print(f'Ultrapassou a outra com {maior_inicialmente}m em {count} anos');

        print(f'\nAtualmente, altura da "menor": {menor_crescimento}');
        print(f'altura da "maior": {maior_crescimento}');
        
        exit();

    count = count + 1;


print('Passaram-se 20 anos e a pessoa "menor" não ultrapassou a "maior".');